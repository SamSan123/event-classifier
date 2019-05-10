from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    
    url(r'^$', views.event_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.event_detail, name="detail"),
]