from celery import shared_task
from .models import Ride
import random

@shared_task
def update_ride_locations():
    rides = Ride.objects.filter(status='in_progress')
    for ride in rides:
        ride.current_location = f"Latitude: {random.uniform(-90, 90)}, Longitude: {random.uniform(-180, 180)}"
        ride.save()
