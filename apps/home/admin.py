# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review','reviewer','rating','created_on')

@admin.register(Css)
class CssAdmin(admin.ModelAdmin):
    list_display = ('content','title','project','created_on')


@admin.register(Js)
class JsAdmin(admin.ModelAdmin):
    list_display = ('content','title','project','created_on')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar','bio','city')
