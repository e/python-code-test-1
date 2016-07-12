from django.db import models
from django.contrib.auth.models import User
from items.models import PhotoItem, TweetItem


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(PhotoItem, null=True, blank=True)
    tweet = models.ForeignKey(TweetItem, null=True, blank=True)
