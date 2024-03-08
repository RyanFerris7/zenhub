from django.urls import path
from . import views
# from .views import PostList
app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='homepage'),
    path('<slug:post>/', views.post_detail, name="post_detail"), 
]