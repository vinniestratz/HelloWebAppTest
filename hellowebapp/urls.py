from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from collection import views
from collection.backends import MyRegistrationView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change,
    password_change_done,
)

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about-us/$', views.about, name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    # redirect view things
    url(r'^things/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail,
        name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$',
        views.edit_thing, name='edit_thing'),
    # redirect view browse
    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
    # our new browse flow
    url(r'^browse/name/$',
        views.browse_by_name, name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$',
        views.browse_by_name, name='browse_by_name'),
    # new password reset urls
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),
    # new url definitions
    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'},
        name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
    # below all one line
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_thing/$',
        views.create_thing,
        name='registration_create_thing'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
