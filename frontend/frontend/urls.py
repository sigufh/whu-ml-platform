"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from machinelearn import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('machinelearn.urls')),
   
    path("register/",views.register,name='register'),
     path("login/",views.login,name='login'),
    path("home/",views.home,name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('user/',views.userinf,name='user'),
    path('information/',views.information,name='information'),
     

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
