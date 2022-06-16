from pyexpat import model
from rest_framework import serializers
from .models import Portfolio, Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class PortfoioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Portfolio
    fields = '__all__'