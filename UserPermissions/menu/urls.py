# coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$',login),
]

