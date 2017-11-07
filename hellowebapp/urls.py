from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views
from collection.backends import MyRegistrationView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about-us/$', views.about, name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail,
        name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$',
        views.edit_thing, name='edit_thing'),
    # new password reset urls
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),
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
