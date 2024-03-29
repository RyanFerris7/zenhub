"""
URL configuration for zenhub_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic.base import TemplateView  # new





urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),  # new
    # - Using empty path incompatible with actual pathing - path("", TemplateView.as_view(template_name="signhome.html"), name="home"),  # new
    path('blog/', include('blog.urls')),
    path('events/', include('events.urls')),
    path('profile/', include('user_profile.urls')),
    path('links/', include('links.urls')),
    path('', include('links.urls')),
    # Add other app URLs as needed
]