from django.conf.urls import include, url
from django.contrib import admin
from .views import home

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),
]
