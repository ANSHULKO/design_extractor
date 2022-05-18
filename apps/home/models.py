# -*- encoding: utf-8 -*-


from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(verbose_name="website")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer", null=True)
    review = models.TextField()
    rating = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review[:100]


class Css(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Js(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    city = models.TextField(max_length=50)

    def __str__(self):
        return self.user.username


