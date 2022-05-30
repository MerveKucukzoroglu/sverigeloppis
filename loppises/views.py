""" Loppis app views file """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Loppis, County

def all_loppises(request):
    """ A view to return list of all the loppises """

    county_list = County.objects.all()
    loppises = Loppis.objects.all()
    query = None
    sort = None
    direction = None
    counties = None

    if request.GET:
        if 'county' in request.GET:
            counties = request.GET['county'].split(',')
            loppises = loppises.filter(county__county__in=counties)
            counties = County.objects.filter(county__in=counties)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('loppises'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(county__county__icontains=query) 
            loppises = loppises.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'county_list': county_list,
        'loppises': loppises,
        'search_term': query,
        'current_counties': counties,
        'current_sorting': current_sorting,
    }

    return render(request, 'loppises/loppises.html', context)


def loppis_detail(request, loppis_id):
    """ A view to show individual loppis details """

    loppis = get_object_or_404(Loppis, pk=loppis_id)

    context = {
        'loppis': loppis,
    }

    return render(request, 'loppises/loppis_detail.html', context)
