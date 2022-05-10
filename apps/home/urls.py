# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pathlib import Path
from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    path('Review/',TemplateView.as_view(template_name='home/Review.html')),
    path('Css/',TemplateView.as_view(template_name='home/Css.html')),
    path('Js/',TemplateView.as_view(template_name='home/Js.html')),
    path('Profile/',TemplateView.as_view(template_name='home/Profile.html')),
    


]
