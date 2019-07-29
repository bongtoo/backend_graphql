from django.db import models

# Create your models here.
class ServiceModel(models.Model):
  title = models.CharField(max_length=200,null=True) # 제목
  term = models.CharField(max_length=200, null=True) # 활동기간
  field = models.CharField(max_length=200, null=True) # 활동분야
  region = models.CharField(max_length=200, null=True) # 활동지역
  place = models.CharField(max_length=200, null=True) # 활동장소
  subject = models.CharField(max_length=200, null=True) # 활동대상
  value = models.CharField(max_length=200, null=True) # ID