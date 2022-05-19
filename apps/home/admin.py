# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review','reviewer','rating')

@admin.register(Css)
class CssAdmin(admin.ModelAdmin):
    list_display = ('content','title','project')


@admin.register(Js)
class JsAdmin(admin.ModelAdmin):
    list_display = ('content','title','project')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','avatar','bio','city')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','url','user','created_on')