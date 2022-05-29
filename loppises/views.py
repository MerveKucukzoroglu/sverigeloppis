""" Loppis app views file """
from django.shortcuts import render, get_object_or_404
from .models import Loppis

def all_loppises(request):
    """ A view to return list of all the loppises """
    loppises = Loppis.objects.all()

    context = {
        'loppises': loppises,
    }
    return render(request, 'loppises/loppises.html', context)


def loppis_detail(request, loppis_id):
    """ A view to show individual loppis details """

    loppis = get_object_or_404(Loppis, pk=loppis_id)

    context = {
        'loppis': loppis,
    }

    return render(request, 'loppises/loppis_detail.html', context)
