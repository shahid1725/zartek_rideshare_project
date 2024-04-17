from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ride(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_requested')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_accepted', null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    current_location = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return f"Ride {self.id} - {self.status}"
    

class Test(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
