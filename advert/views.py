"""Loppis Advertisement views"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoppisForm
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
            return redirect(reverse('advert'))
        else:
            messages.error(request, 'Failed to add Loppis. Please ensure the form is valid.')
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
