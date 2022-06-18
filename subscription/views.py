from django.shortcuts import render
from .forms import NewsletterForm
from django.contrib import messages
from .models import Subscriptions


def subscribe(request):
    """ A view to show individual loppis details """
    newsletter_form = NewsletterForm(data=request.POST)
    
    if request.method == 'POST':
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get("email")
            if email:
                messages.success(request, 'Successfully subscribed to our Newsletter!')
            else:
                messages.error(request, 'This email already exists!')
            newsletter_form.save()
        else:
            messages.error(request, 'This email already exists!')
            newsletter_form = NewsletterForm()

    context = {
        'newsletter_form': NewsletterForm(),
    }

    return render(request, 'subscription/subscribe.html', context)
