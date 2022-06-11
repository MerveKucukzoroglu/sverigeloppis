from django.shortcuts import render


def advert(request):
    """Loppis Advertisement View"""
    template = 'advert/advert.html'
    return render(request, template)
