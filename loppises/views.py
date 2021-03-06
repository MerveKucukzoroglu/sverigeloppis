""" Loppis app views file """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from advert.forms import LoppisForm
from questions.forms import QuestionForm

from .models import Loppis, County


def all_loppises(request):
    """ A view to return list of all the loppises """

    county_list = County.objects.all().order_by("county")
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
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('loppises'))

            queries = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(county__county__icontains=query)
                )
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
    questions = loppis.questions.order_by('created_on')
    question_form = QuestionForm(data=request.POST)

    if question_form.is_valid():
        question_form.instance.email = request.user.email
        question_form.instance.author = request.user.username
        question = question_form.save(commit=False)
        question.loppis = loppis
        question.save()
    else:
        question_form = QuestionForm()

    context = {
        'questions': questions,
        'question_form': QuestionForm(),
        'loppis': loppis,
    }

    return render(request, 'loppises/loppis_detail.html', context)


@login_required
def edit_loppis(request, loppis_id):
    """ Edit a loppis in the announcement """
    loppis = get_object_or_404(Loppis, pk=loppis_id)
    if not request.user == loppis.seller:
        messages.error(request, 'Sorry, only loppis owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LoppisForm(request.POST, request.FILES, instance=loppis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your Loppis!')
            return redirect(reverse('loppis_detail', args=[loppis.id]))
        else:
            messages.error(
                request,
                'Failed to update Loppis. Please ensure the form is valid.'
                )
    else:
        form = LoppisForm(instance=loppis)
        messages.info(request, f'You are editing {loppis.title}')
        form.fields['country'].widget.attrs['readonly'] = True
        form.fields['start_date'].widget.attrs['readonly'] = True
        form.fields['end_date'].widget.attrs['readonly'] = True

    template = 'loppises/edit_loppis.html'
    context = {
        'form': form,
        'loppis': loppis,
    }

    return render(request, template, context)


@login_required
def delete_loppis(request, loppis_id):
    """ Delete a loppis """
    loppis = get_object_or_404(Loppis, id=loppis_id)
    if not request.user == loppis.seller:
        messages.error(request, 'Sorry, only loppis owner can do that.')
        return redirect(reverse('home'))

    loppis.delete()
    messages.success(request, 'Loppis Deleted!')
    return redirect(reverse('loppises'))
