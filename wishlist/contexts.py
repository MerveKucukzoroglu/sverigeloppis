from django.conf import settings

def wishlist_contents(request):

    wishlist_items = []
    loppis_count = 0

    context = {
        'wishlist_items': wishlist_items,
        'loppis_count': loppis_count,
    }

    return context
