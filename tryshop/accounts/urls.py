from django.conf.urls import patterns, url

from django.contrib.auth import views as auth_views

urlpatterns = patterns('tryshop.accounts.views',
    url(r'^accounts/register/$',
        'register',
        name='accounts_register'),
)
