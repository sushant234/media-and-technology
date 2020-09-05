from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.servicess,name='services'),
    path('blog',views.blogs,name='blog'),
    url(r'^single_blog/(?P<value>\d+)/$', views.single_blogs,name='single_blog'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
