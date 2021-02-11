from django.urls import path, include
from django.conf.urls.static import static
from blog.views import blog_all, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.project, name='project'),
    path('blog/', include('blog.urls', namespace='blog')),
]