from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField(default='placeholder')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username + ' Profile'