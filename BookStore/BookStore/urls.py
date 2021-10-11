"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include 
from BookApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('contact/',views.contactus),
    path('login/',views.LogIn),
    path('checkLogin/',views.CheckLogin),
    path('register/',views.Register),
    path('reguser/',views.RegNewUser),
    path('home/',views.home),
    path('cbse/',views.CBSE),
    path('gseb/',views.GSEB),
    path('cbses1/',views.CBSES1), 
    path('cbses2/',views.CBSES2),
    path('cbses3/',views.CBSES3),
    path('cbses4/',views.CBSES4),
    path('cbses5/',views.CBSES5),
    path('cbses6/',views.CBSES6),
    path('cbses7/',views.CBSES7),
    path('cbses8/',views.CBSES8),
    path('cbses9/',views.CBSES9),
    path('cbses10/',views.CBSES10),
    path('brushes/',views.Brush),
    path('color/',views.Color),
    path('sketchbook/',views.Sketchbook),
    path('singleline/',views.Singleline),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)