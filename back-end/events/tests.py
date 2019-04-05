from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tweet
from django.urls import include, path, reverse
from .serializers import TweeTSerializer

# Create your tests here.
class APITEST(TestCase):
    def setUp(self):
     self.client = APIClient()
    def test_events_get(self):
         tweets = Tweet.objects.all()
         url = reverse('events')
         response = self.client.get(url)
         serializer = TweeTSerializer(tweets,many=True)
         self.assertContains(response, serializer.data)
