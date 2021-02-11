from django.db import models

# Create your models here.

#models are like tables in the database and a class is en entity inside the table 
#the class have objects = instances 
#instances have attributtes
class Project(models.Model):
	title       = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	image       = models.ImageField(upload_to='portfolio/images/')
	url         = models.URLField(blank=True)#if you look at the project in the admin 
#you will find that isn't bold because it's optional unlike description and image