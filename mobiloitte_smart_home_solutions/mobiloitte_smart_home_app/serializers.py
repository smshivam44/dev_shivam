from rest_framework import serializers
from .models import AppUser




class LoginSerializer(serializers.ModelSerializer):
    """Serializer for app user"""

    class Meta:
        """docstring for meta"""
        model = AppUser
        fields = ('id', 'name', 'email')