from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile, Booking
from .forms import UserProfileForm

# Create your views here.
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile.html', {'form': form})

def view_bookings(request):
    # Retrieve bookings associated with the currently logged-in user
    user_bookings = Booking.objects.filter(user=request.user)

    # Pass bookings to the template context
    context = {'user_bookings': user_bookings}
    return render(request, 'bookings.html', context)

def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.user == booking.user:
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this booking!')
    return redirect('profile')