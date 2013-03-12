from django.conf.urls.defaults import patterns, include, url

from website.views import HomeView


urlpatterns = patterns('',
    url(r'^home',HomeView.as_view(),name="home"),
)  

