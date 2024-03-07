from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
EVENT_TYPES = (
    ("Fitness Class", "Fitness Class"),
    ("Yoga Class", "Yoga Class"),
    ("Life Coaching", "Life Coaching"),
    )


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField(default='placeholder')
    type = models.CharField(max_length=50, choices=EVENT_TYPES, default="Fitness Class")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor_events', null=True, blank=True) #related name to access events associated with a specific instructor from the User model.
    description = models.TextField(default="")
    time = models.DateTimeField()
    available_slots = models.PositiveIntegerField(default=1)
    current_slots = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
