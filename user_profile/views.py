from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from events.models import Booking
from .forms import UserProfileForm

def profile(request):
    #Fetch or create UserProfile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    #Get user's bookings
    user_bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    # Pass form and bookings to the template context
    return render(request, 'profile.html', {'form': form, 'user_bookings': user_bookings})

def view_bookings(request):
    # Retrieve bookings associated with the currently logged-in user
    user_bookings = Booking.objects.filter(user=request.user)
    print(user_bookings)
    # Pass bookings to the template context
    context = {'user_bookings': user_bookings}
    return render(request, 'profile.html', context)

def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.user == booking.user:
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this booking!')
    return redirect('profile')