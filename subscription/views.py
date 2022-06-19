"""Newsletter Subscription Views file"""
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import NewsletterForm


def subscribe(request):
    """ A view to show individual loppis details """
    newsletter_form = NewsletterForm(data=request.POST)

    if request.method == 'POST':
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get("email")
            if email:
                messages.success(
                    request, 'Successfully subscribed to our Newsletter!'
                    )
                subscriber_email = email
                subject = render_to_string(
                        'subscription/confirmation_emails/confirmation_email_subject.txt',
                        {'email': email})
                body = render_to_string(
                        'subscription/confirmation_emails/confirmation_email_body.txt',
                        {
                            'email': email,
                            'subscriber_email': subscriber_email,
                            'contact_email': settings.DEFAULT_FROM_EMAIL
                        })
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber_email]
                )
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
