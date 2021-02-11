from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_all, name='blog_all'), 
    path('<int:blog_id>/', views.detail, name='detail'),
]