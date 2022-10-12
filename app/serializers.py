from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        
class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'