from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Event, Booking
from .forms import BookingForm
from django.contrib import messages

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    form = BookingForm()
    return render(request, 'event_detail.html', {'event': event, 'form': form})

def book_event(request, event_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("Attempting to submit form")

        if form.is_valid():
            event = Event.objects.get(id=event_id)
            current_slots = Booking.objects.filter(event=event).count()  # Retrieve current slots

            if event.available_slots >= current_slots:
                booking = form.save(commit=False)
                booking.event = event
                booking.user = request.user # Set the booking user
                booking.save()
                event.current_slots -= 1
                event.save()

                print("Form Post successful")

                 # Inform the user that their booking has been received
                messages.success(request, 'Your booking has been received!')

                return redirect('event_list')
            else:
                # Handle case when no available slots left
                return render(request, 'no_slots_available.html')
    else:
        form = BookingForm()
        return render(request, 'event_detail.html', {'form': form})