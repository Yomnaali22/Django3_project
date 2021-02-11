from django.shortcuts import render
from .models import Project
from blog.views import (blog_all, detail)
# Create your views here.

def project(request):
    projects = Project.objects.all()#this graps all data from database which we created in models.py to display it 
    return render(request, 'project.html', {'projects': projects})