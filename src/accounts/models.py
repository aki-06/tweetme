from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by', blank=True)

    def __str__(self):
        return str(self.following.all().count())
