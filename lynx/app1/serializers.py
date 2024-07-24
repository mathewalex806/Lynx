from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Camera, Community, User_Community, Camera_Community


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]
        extra_kwargs = {'password': {'write_only': True}}  # Ensures the password is write-only

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
    
class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ["name","latitude","longitude"]
    def create(self,validated_data):
        camera = Camera(name = validated_data["name"],
                        latitude = validated_data["latitude"],
                        longitude  = validated_data["longitude"]
                        )
        camera.save()
        return camera
        

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["name","description","city","locality","country"]

    def create(self, validated_data):
        community_ser = Community(name= validated_data["name"],
                                  description= validated_data["description"],
                                  city= validated_data["city"],
                                  locality= validated_data["locality"],
                                  country= validated_data["country"])
    
        community_ser.save()
        return community_ser