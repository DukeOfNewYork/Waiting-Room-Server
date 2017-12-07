from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^output$', views.output, name='output'),
    url(r'^input', views.input, name='input'),
    url(r'^monitoring', views.monitoring, name='monitoring'),
    url(r'^administration', views.administration, name='administration'),
]
