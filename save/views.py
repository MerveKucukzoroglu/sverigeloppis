""" Save app views file """
from django.shortcuts import render

def view_save(request):
    """ A view to return the saves page """
    return render(request, 'save/save.html')
