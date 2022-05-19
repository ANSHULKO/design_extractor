from django import forms
from django.contrib import admin
from .models import *


class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Review(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('review','reviewer','rating',)

class Css(forms.ModelForm):
    
    class Meta:
        model = Css 
        fields = ('content','title','project')


class Js(forms.ModelForm):
    
    class Meta:
        model = Js 
        fields = ('content','title','project')


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        
        fields = ('firstname','lastname','avatar','bio','city')