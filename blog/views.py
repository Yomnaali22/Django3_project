from django.shortcuts import render, get_object_or_404
from .models import Blog #this is the object
# Create your views here.

def blog_all(request):
	blog_all = Blog.objects.all()#this is Blog model
	return render(request, 'blogss.html', {'blog_all': blog_all})#why I needed to put the variable in the dictionar??


def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)#pk is a database term which refers to the object exits in the datebase
	return render(request, 'detail.html', {'id':blog})