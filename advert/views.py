"""Loppis Advertisement views"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoppisForm
from django.contrib.auth.models import User


@login_required
def advert(request):
    """Loppis Advertisement View"""
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
        form = LoppisForm()
        form.fields['country'].widget.attrs['readonly'] = True
    template = 'advert/advert.html'
    context = {
        'form': form,
        'stripe_public_key': 'pk_test_51KrjN6A64mxey4Bo5lacxcOm1dPcgSbVhBV9VDT9Tw5UZf0ZFCcbKDfYt9z1KQNcN8ZvjFBtD0OmtTSLAaMVbIhj00kFxQnHLi',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
