
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from login_system import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('login/', views.login, name='login'),#everything blog related go ahead and forward it to the blog app
]

