from django.shortcuts import render
from loppises.models import Loppis
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)

@login_required
def my_loppises(request):
    """Authenticated user views their own poems"""
    logged_in_user = request.user
    logged_in_user_loppises = Loppis.objects.filter(seller=logged_in_user)
    return render(request, 'profiles/my_loppises.html', {'loppises': logged_in_user_loppises})
