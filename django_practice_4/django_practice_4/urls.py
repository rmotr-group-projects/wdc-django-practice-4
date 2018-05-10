"""django_practice_4 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from artists import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication URLs using Django built-in views
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),

    path('artists/', views.artists, name='artists'),
    path('delete-song/', views.delete_song, name='delete_song'),
    path('delete-artist/', views.delete_artist, name='delete_artist'),
]
