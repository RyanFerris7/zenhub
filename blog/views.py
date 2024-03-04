from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):

    all_posts = Post.objects.all()
    return render(request, 'index.html', {'post' : post})
