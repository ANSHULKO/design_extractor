# -*- encoding: utf-8 -*

from pathlib import Path
from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path('review/', project_reviews, name='project_reviews'),
    path('css/', project_css, name='css'),
    path('js/', project_js, name='js'),
    path('profile/', profile_detail, name='profile'),
    path('project/<int:id>',project_details, name='project_detail'),
    path('add_website/', add_website, name='add_website'),
    # re_path(r'^.*\.*', views.pages, name='pages'),


]
