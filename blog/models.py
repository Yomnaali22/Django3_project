from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
	title       = models.CharField(max_length=200)
	date        = models.DateField()
	description = models.TextField()