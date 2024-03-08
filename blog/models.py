from django.db import models

# Create your models here.
# 
# RULES 
#
# 1. Do not edit or adjust anyone else's code.
#
# 2. If something needs to be changed, just ask 
#    the person who wrote it. 
#
# 3. Add as many lines as you need to your sections.
#
# 4. Use comments to to help everyone else read the 
#    code and understand what it does. 
#
# 5. Always pull before pushing, it'll help prevent
#    merge conflicts. 


# Arianne's Code
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

CATEGORIES = (
    ("Fitness", "Fitness"),
    ("Mental Wellbeing", "Mental Wellbeing"),
    ("Life Coaching", "Life Coaching"),
    ("General", "General"),
)
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField(default='placeholder')
    category = models.CharField(max_length=50, choices=CATEGORIES, default="General")
    content = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    publish = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.slug)])
    
    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f"Comment by {self.username}"





# ---------- 


# Cian's Code 








# ---------- 


# Ryan's Code 









# ---------- 


# Tuguldur's Code 










# ---------- 