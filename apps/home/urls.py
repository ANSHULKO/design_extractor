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
    path('css/', view_css, name='css'),
    path('js/', view_js, name='js'),
    path('profile/', profile_detail, name='profile'),
    path('profile/edit/', edit_profile, name='profile_edit'),
    path('project/<int:id>',project_details, name='project_detail'),
    path('project/<int:id>/css',project_css, name='project_css'),
    path('project/<int:id>/js',project_js, name='project_js'),
    path('add_website/', add_website, name='add_website'),
    path('extract/', extract_website, name='extract_website'),
    path('delete/<int:id>', delete_project, name='delete_project'),
    path('css/download/<int:id>', download_css, name='download_css'),   
    path('css/delete/<int:id>', delete_css, name='delete_css'),
    path('js/download/<int:id>', download_js, name='download_js'),
    path('js/delete/<int:id>', delete_js, name='delete_js'),
    # re_path(r'^.*\.*', views.pages, name='pages'),


]
