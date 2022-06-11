"""Loppis Advertisement views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoppisForm
from loppises.models import Loppis
from .models import Advert

from django.contrib.auth.models import User
from django.conf import settings

import stripe

@login_required
def advert(request):
    """Loppis Advertisement View"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form = LoppisForm(request.POST, request.FILES)
        if form.is_valid():
            loppis = form.save(commit=False)
            loppis.seller = User.objects.get(username=request.user.username)
            messages.success(request, 'Successfully published Loppis!')
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


def advert_success(request):
    """ Handle successfull payment """
    save_info = request.session.get('save_info')
    messages.success(request, f'Loppis published successfully! \
        A confirmation email will be send.')

    template = 'advert/advert_success.html'

    return render(request, template)
