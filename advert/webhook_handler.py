from django.http import HttpResponse
from .models import Advert
from loppises.models import Loppis


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
        
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        try:
            intent = event.data.object
            pid = intent.id
            stripe_pid=pid
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)
        
        except Exception as e:
            if advert:
                advert.delete()
            return HttpResponse(content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
            status=500)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
