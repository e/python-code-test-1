from django.db import models
from django.contrib.auth.models import User


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PhotoItem(ItemAbstract):
    image = models.ImageField(upload_to='photos')


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)
