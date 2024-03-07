from django.urls import path
from .views import event_list, event_detail, book_event


urlpatterns = [
    path("", event_list, name="event_list"),
    path('event_detail/<int:event_id>/', event_detail, name='event_detail'),
    path('book_event/<int:event_id>/', book_event, name='book_event'),
]