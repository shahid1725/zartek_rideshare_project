import time
from django.core.management.base import BaseCommand
from rideshare.rides.models import *
import random

class Command(BaseCommand):
    help = 'Updates the current location of rides'

    def handle(self, *args, **options):
        while True:
            rides = Ride.objects.filter(status='in_progress')  # Get rides in progress
            for ride in rides:
                # Simulate updating the location (replace with your logic)
                ride.current_location = f"Latitude: {random.uniform(-90, 90)}, Longitude: {random.uniform(-180, 180)}"
                ride.save()
            time.sleep(60)  # Update every 60 seconds
