from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
EVENT_TYPES = (
    ("Fitness Class", "Fitness Class"),
    ("Yoga Class", "Yoga Class"),
    ("Life Coaching", "Life Coaching"),
    )


class Event(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=EVENT_TYPES, default="Fitness Class")
    time = models.DateTimeField()
    available_slots = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

# EVENT_CHOICES = (
#     ("Fitness Class", "Fitness Class"),
#     ("Yoga Class", "Yoga Class"),
#     ("Life Coaching", "Life Coaching"),
#     )

# TIME_CHOICES = (
#     ("8AM","8AM"),
#     ("10AM","10AM"),
#     ("12PM","12PM"),
#     ("2PM","2PM"),
#     ("4PM","4PM"),
#     ("6PM","6PM"),
# )

# class Appointment(models.Model):
#     """
#     Class to store Appointment data. Collects 5 data points, user, event, day, time and time ordered. 
#     2 additional data points are slots available and slots filled, to change how many slots are available based on the event type
#     """
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     event = models.CharField(max_length=50, choices=EVENT_CHOICES, default="Fitness Class")
#     day = models.DateField(default=datetime.now)
#     time = models.CharField(max_length=10, choices=TIME_CHOICES, default="8am")
#     time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    
#     slots_available = models.IntegerField(default=1)
#     slots_filled = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.user.username} | day: {self.day} | time: {self.time}"