from django.conf.urls import patterns, url

urlpatterns = patterns('tryshop.website.views',
    url(r'^$', 'index', name='index'),
)
