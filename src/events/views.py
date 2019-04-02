
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from slackclient import SlackClient 
from .models import Tweet
from django.views import generic
from .serializers import TweeTSerializer
import tweepy
 
class Events(APIView):
    def __init__(self):
      #setting tweeter credintials
        self.CONSUMER_KEY = getattr(settings, 'CONSUMER_KEY', None)
        self.CONSUMER_SECRET =getattr(settings, 'CONSUMER_SECRET', None)
        self.ACCESS_KEY =getattr(settings, 'ACCESS_KEY', None)
        self.ACCESS_SECRET =getattr(settings, 'ACCESS_SECRET', None)
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
        #setting slack credintials
        self.SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
        self.SLACK_BOT_USER_TOKEN = getattr(settings,'SLACK_BOT_USER_TOKEN', None) 
        self.Client = SlackClient(self.SLACK_BOT_USER_TOKEN)  
    def post(self,req,*args,**kwargs):
        message=req.data 
        if message.get('token') != self.SLACK_VERIFICATION_TOKEN:
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
                
                event_id=message.get('event_id')
                text = text.replace('go','')
                print(text)
                print(bot_text)
                if self.Client.api_call(method="chat.postMessage",channel = channel,text = bot_text,):
                    print(Tweet.objects.filter(tweet=text).values('created'))
                # check if status alrdy exists and save to the data base
                if Tweet.objects.filter(tweet=text):
                    return Response(status=status.HTTP_403_FORBIDDEN)
                new_tweet=Tweet(user=new_user,tweet=text)
                new_tweet.save()
                self.api.update_status(text)

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
