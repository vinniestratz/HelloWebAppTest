from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    things = Thing.objects.all()
    # correct_thing = Thing.objects.get(name='Hello')
    # things = Thing.objects.filter(name='Hello')
    return render(request, 'index.html', {
        'things': things,
        })


def thing_detail(request, slug):
    # grab object
    thing = Thing.objects.get(slug=slug)
    # pass to template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })


@login_required
def edit_thing(request, slug):
    # grab object
    thing = Thing.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if thing.user != request.user:
        raise Http404

    # set the form we're using
    form_class = ThingForm
    # if we're coming to this view from a submitted form_class
    if request.method == 'POST':
        # grab the data from the submitted form_class
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save data
            form.save()
            return redirect('thing_detail', slug=thing.slug)

        # otherwise just create the form
    else:
        form = form_class(instance=thing)

        # and render the template
        return render(request, 'things/edit_thing.html', {
            'thing': thing,
            'form': form,
            })


def create_thing(request):
    form_class = ThingForm
    # if coming from submitted form do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            thing = form.save(commit=False)
            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)
            # save the object
            thing.save()
            # redirect to out newly created thing
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class()

        return render(request, 'things/create_thing.html', {
            'form': form,
            })


def browse_by_name(request, initial=None):
    if initial:
        things = Thing.objects.filter(name__istartswith=initial)
        things = things.order_by('name')
    else:
        things = Thing.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'things': things,
        'initial': initial,
    })


def about(request):
    # new view
    return render(request, 'about.html')
