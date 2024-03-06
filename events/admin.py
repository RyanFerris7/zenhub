from django.contrib import admin
from .models import Event, Booking

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'time', 'available_slots', 'current_slots')
    inlines = [BookingInline]
