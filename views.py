from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from slackclient import SlackClient 
from .models import Tweet
from django.views import generic
from .serializers import TweeTSerializer
import tweepy
# Create your views here.
#setting tweeter credintials
CONSUMER_KEY = getattr(settings, 'CONSUMER_KEY', None)
CONSUMER_SECRET =getattr(settings, 'CONSUMER_SECRET', None)
ACCESS_KEY =getattr(settings, 'ACCESS_KEY', None)
ACCESS_SECRET =getattr(settings, 'ACCESS_SECRET', None)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#setting slack credintials
SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,'SLACK_BOT_USER_TOKEN', None) 
Client = SlackClient(SLACK_BOT_USER_TOKEN)   
class Events(APIView):
    
    def post(self,req,*args,**kwargs):
        event_id=" "
        message=req.data 
        if message.get('token') != SLACK_VERIFICATION_TOKEN:
           return Response(status=status.HTTP_403_FORBIDDEN)
        # verification challenge
        if message.get('url') == 'url_verification':
            return Response(status=status.HTTP_200_OK)
        #challenge param
        if message.get('challenge'):
            return Response(message.get('challenge'))
        # catching ok messages
        if 'event' in message:
            event_message = message.get('event')
            
            
            new_user = event_message.get('user')
            text     = event_message.get('text')
            channel  = event_message.get('channel')
            bot_text = "post saved ".format()
            if "go" in text.lower():
                if event_id == message.get('event_id'):
                    print('event id'+event_id)
                    return Response(status=status.HTTP_200_OK)
                event_id=message.get('event_id')
                text = text.replace('go','')
                print(text)
                print(bot_text)
                Client.api_call(
                    method="chat.postMessage",
                    channel = channel,
                    text = bot_text,
                )
                # save to the data base
                if Tweet.objects.filter(tweet=text):
                    return Response(status=status.HTTP_200_OK)
                new_tweet=Tweet(user=new_user,tweet=text)
                new_tweet.save()
                api.update_status(text)

                return Response(status=status.HTTP_200_OK)
             
        
        return Response(status.HTTP_200_OK)
    def get(self,req,*args,**kwargs):
        created = self.request.query_params.get('created')
        print(created)
        #get all tweets from database and sort by created
        tweets = Tweet.objects.all().order_by('-created')
        #serialize data
        serializer = TweeTSerializer(tweets,many=True)
        return Response(serializer.data)
