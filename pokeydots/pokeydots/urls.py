from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', login_required(views.HomeView.as_view()), name="home"),
    url(r'^admin/', include(admin.site.urls)),
)
