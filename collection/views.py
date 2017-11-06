from django.shortcuts import render
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


def about(request):
    # new view
    return render(request, 'about.html')
