from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class add(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    host = models.ForeignKey(User,on_delete=models.CASCADE)

class HistoryModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    host = models.ForeignKey(User,on_delete=models.CASCADE)

class CompleteModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    host = models.ForeignKey(User,on_delete=models.CASCADE)

