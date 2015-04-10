from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
# from Alumni import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Alumni.urls')),
)
