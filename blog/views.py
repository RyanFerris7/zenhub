from django.shortcuts import render, get_object_or_404, reverse

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
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import NewCommentForm


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    # paginate_by = 4
    context_object_name = 'post_list'

def post_detail(request, post):

    post = get_object_or_404(Post, slug=post, status=1)

    comments = post.comments.filter(approved=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.username = request.user
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})









# ---------- 


# Cian's Code 








# ---------- 


# Ryan's Code 









# ---------- 


# Tuguldur's Code 










# ---------- 