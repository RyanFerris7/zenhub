from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from events.models import Booking

# Define inline admin model for Booking
class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

# Extend the UserAdmin
class CustomUserAdmin(UserAdmin):
    inlines = [BookingInline]

# Register models
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)