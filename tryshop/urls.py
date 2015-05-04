from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tryshop.website.urls')),
    url(r'^', include('tryshop.accounts.urls')),
    # url(r'^', include('tryshop.pages.urls')),
    # rl(r'^', include('tryshop.product.urls')),
)
