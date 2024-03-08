from django.urls import path
from .views import home, team

urlpatterns = [
    path('', home, name='home'),
    path('team', team, name='team')
]