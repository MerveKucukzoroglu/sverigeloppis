""" Advert App urls file """
from django.urls import path
from . import views
# from .webhooks import webhook

urlpatterns = [
    path('', views.advert, name='advert'),
    path('advert_success/', views.advert_success, name='advert_success'),
    path(
        'cache_advert_data/', views.cache_advert_data, name='cache_advert_data'
        ),
    # path('wh/', webhook, name='webhook'),
]
