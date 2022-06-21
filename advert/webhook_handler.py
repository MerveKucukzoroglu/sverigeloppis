# """Webhook Handler"""
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings
# from django.contrib.auth.models import User
# from loppises.models import Loppis
# from .forms import LoppisForm
# from .models import Advert


# class StripeWH_Handler:
#     """Handle Stripe webhooks"""

#     def __init__(self, request):
#         self.request = request

#     def _send_confirmation_email(self, advert):
#         """Send user confirmation email"""
        
#         advert = Advert.objects.all()
#         # field_name = 'email'
#         # User.objects.get(uesrname=username)
#         loppis = Loppis.objects.first()
#         # field_value = getattr(user, field_name)
#         # logged_in_user = request.user
#         # logged_in_user_email = Loppis.objects.filter(seller=logged_in_user)
#         seller_email = User.email
#         print(seller_email)
#         subject = render_to_string(
#             'advert/confirmation_emails/confirmation_email_subject.txt',
#             {'advert': advert})
#         body = render_to_string(
#             'advert/confirmation_emails/confirmation_email_body.txt',
#             {
#                 'advert': advert,
#                 'seller_email': seller_email,
#                 'loppis': loppis,
#                 'contact_email': settings.DEFAULT_FROM_EMAIL
#             })

#         send_mail(
#             subject,
#             body,
#             settings.DEFAULT_FROM_EMAIL,
#             [seller_email]
#         )

#     def handle_event(self, event):
#         """
#         Handle a generic/unknown/unexpected webhook event
#         """
#         advert = Advert.objects.all()
#         # self._send_confirmation_email(advert)
#         return HttpResponse(
#             content=f'Unhandled webhook received: {event["type"]}',
#             status=200)

#     def handle_payment_intent_succeeded(self, event):
#         """
#         Handle the payment_intent.succeeded webhook from Stripe
#         """
#         try:
#             intent=event.data.object
#             pid=intent.id
#             stripe_pid=pid
#             advert=Advert.objects.all()
#             self._send_confirmation_email(advert)
#             return HttpResponse(
#                 content=f'Webhook received: {event["type"]}',
#                 status=200)

#         except Exception as e:
#             if advert:
#                 advert.delete()
#                 # self._send_confirmation_email(advert)
#             return HttpResponse(
#                 content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
#                 status=500
#             )
#         self._send_confirmation_email(advert)

#     def handle_payment_intent_payment_failed(self, event):
#         """
#         Handle the payment_intent.payment_failed webhook from Stripe
#         """
#         return HttpResponse(
#             content=f'Webhook received: {event["type"]}',
#             status=200)
