"""Wishlist App context file"""
from django.shortcuts import get_object_or_404
from loppises.models import Loppis


def wishlist_contents(request):
    """wishlist content function"""
    wishlist_items = []
    loppis_count = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, quantity in wishlist.items():
        loppis = get_object_or_404(Loppis, pk=item_id)
        loppis_count = quantity
        wishlist_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'loppis': loppis,
        })

    context = {
        'wishlist_items': wishlist_items,
        'loppis_count': loppis_count,
    }

    return context
