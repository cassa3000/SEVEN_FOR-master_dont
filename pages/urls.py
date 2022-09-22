from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
