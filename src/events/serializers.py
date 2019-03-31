from .models import Tweet
from rest_framework import serializers

class TweeTSerializer(serializers.ModelSerializer):
 class Meta:
     model = Tweet
     fields=('user','tweet','created')