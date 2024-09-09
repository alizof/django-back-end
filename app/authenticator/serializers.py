# Libs
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    
class TokenValidationSerializer(serializers.Serializer):
    token = serializers.CharField()
    