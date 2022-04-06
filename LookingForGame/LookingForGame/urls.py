"""LookingForGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from user import views as user_views

urlpatterns = [
    path('', core_views.index),
    path('profile/', core_views.profile),
    path('about/', core_views.about_us),
    path('lfg/', core_views.lfg),
    path('admin/', admin.site.urls),
    path('join/', core_views.join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),
    path('create_group/', core_views.create_group),
    path('user/', user_views.user),
    path('preferences/', user_views.preferences)
]
