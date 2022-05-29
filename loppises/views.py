""" Loppis app views file """
from django.shortcuts import render
from .models import Loppis

def all_loppises(request):
    """ A view to return list of all the loppises """
    loppises = Loppis.objects.all()

    context = {
        'loppises': loppises,
    }
    return render(request, 'loppises/loppises.html', context)
