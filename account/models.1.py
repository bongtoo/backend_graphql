from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    regionname = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.regionname


class Activity(models.Model):
    activityname = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.activityname


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255)
    region = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, null=True, on_delete=models.CASCADE)
    grandcity = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    profile_image = models.ImageField(
        upload_to='images/', null=True, max_length=None, blank=True)
