from django.db import models

# Create your models here.
class Tweet(models.Model):
    user = models.CharField(max_length=100)
    tweet=models.CharField(max_length=148)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
        