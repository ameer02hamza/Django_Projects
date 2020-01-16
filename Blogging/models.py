from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone


# Create your models here.

class blogs(models.Model):
    post_title = models.CharField(max_length=50, default=None)
    post_Date = models.DateField(default=timezone.now())
    post_content = models.TextField(default=None)
    owner_email = models.CharField(max_length=20)

    def __str__(self):
        return self.post_title


class comments(models.Model):
    post = models.ForeignKey(blogs, on_delete=models.CASCADE, related_name='comment', default=None)
    comment_content = models.TextField(default=None)
    owner_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usernames', default=None)
    comment_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.comment_content


