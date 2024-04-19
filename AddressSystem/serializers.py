from rest_framework import serializers
from .models import Contact, Person, loginModel
from django.contrib.auth.models import User

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginModel
        fields = ['username', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person 
        fields = ['first_name', "middle_name", 'last_name', 'photo', 'Gender']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["Tel_Number", "Address"]