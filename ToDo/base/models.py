from django.db import models

# Create your models here.

class todoModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()

    
class historyModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()


class restoreModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()