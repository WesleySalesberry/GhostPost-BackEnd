from django.db import models
from django.utils import timezone
import secrets
from .utils import secret_token


class PostModel(models.Model):
    isBoast = models.BooleanField(default=True)
    post = models.CharField(max_length=150)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    secret_key = models.CharField(
        max_length=6, default=secret_token)
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post
