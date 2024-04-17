from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

#---------------------------------------------------------------------------------
class RideSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ride
        fields = "__all__"

class RideStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['name', 'phone']