from django.db import models

# Create your models here.
class ServiceModel(models.Model):
  title = models.CharField(max_length=200,null=True)