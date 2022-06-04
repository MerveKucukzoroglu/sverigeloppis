from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from loppises.models import Loppis

# Create your views here.

def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add loppis item to wishlist """

    loppis = Loppis.objects.get(pk=item_id)
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    wishlist[item_id] = quantity
    messages.success(request, f'Added {loppis.title} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    """Remove the item from the wishlist"""

    try:
        wishlist = request.session.get('wishlist', {})
        wishlist.pop(item_id)

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)
