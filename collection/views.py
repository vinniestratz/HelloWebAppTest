from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing


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


def edit_thing(request, slug):
    # grab object
    thing = Thing.objects.get(slug=slug)
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


def about(request):
    # new view
    return render(request, 'about.html')
