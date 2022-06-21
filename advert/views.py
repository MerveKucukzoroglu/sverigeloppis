"""Loppis Advertisement views"""
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.conf import settings
import stripe
from django.core.mail import send_mail
from django.template.loader import render_to_string

from loppises.models import Loppis
from .forms import LoppisForm
from .models import Advert


@require_POST
def cache_advert_data(request):
    """Cache advert exception"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def advert(request):
    """Loppis Advertisement View"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        loppis_form = LoppisForm(request.POST, request.FILES)
        if loppis_form.is_valid():
            loppis = loppis_form.save(commit=False)
            loppis.seller = User.objects.get(username=request.user.username)
            messages.success(request, 'Successfully published Loppis!')
            pid = request.POST.get('client_secret').split('_secret')[0]
            loppis.stripe_pid = pid
            loppis.save()
            return redirect(reverse('advert_success'))
        else:
            messages.error(request, 'Failed to add Loppis. \
                Please double check your information.')
    else:
        stripe_total = round(5 * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        form = LoppisForm()
        form.fields['country'].widget.attrs['readonly'] = True

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'advert/advert.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def send_confirmation_email(request, loppis):
    """
    Send the user a confirmation email
    """
    loppis_advert = Advert.objects.all()
    loppis = Loppis.objects.first()
    if request.user.is_authenticated:
        logged_in_user = loppis.seller
    seller_email = logged_in_user.email

    subject = render_to_string(
        'advert/confirmation_emails/confirmation_email_subject.txt',
        {'loppis_advert': loppis_advert})
    body = render_to_string(
        'advert/confirmation_emails/confirmation_email_body.txt',
        {
            'loppis_advert': loppis_advert,
            'seller_email': seller_email,
            'loppis': loppis,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        })

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [seller_email]
    )


def advert_success(request):
    """ Handle successfull payment """
    advertisement = Advert.objects.all()
    loppis = Loppis.objects.first()
    send_confirmation_email(request, loppis=loppis)
    messages.success(
        request,
        "Loppis published successfully! A confirmation email will be send."
        )

    template = 'advert/advert_success.html'
    context = {
        'advertisement': advertisement
    }

    return render(request, template, context)
