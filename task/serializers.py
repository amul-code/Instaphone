from rest_framework import serializers
from .models import User, Contact, SpamNumber

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'contact_name', 'contact_number']

class SpamNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamNumber
        fields = ['id', 'number', 'reported_by']
