from django.urls import path
from .views import profile, view_bookings, delete_booking

urlpatterns = [
    path('', profile, name='profile'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
]