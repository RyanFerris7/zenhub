from django.shortcuts import render, get_object_or_404

# Create your views here.
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
# from django.views import generic
from django.contrib import messages
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# class PostList(ListView):
#     queryset = Post.objects.filter(status=1)
#     template_name = "blog/index.html"
#     paginate_by = 4
def home(request):

    all_posts = Post.objects.all()
    
    return render(request, 'blog/index.html', {'post': all_posts})










# ---------- 


# Cian's Code 








# ---------- 


# Ryan's Code 









# ---------- 


# Tuguldur's Code 










# ---------- 