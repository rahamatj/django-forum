from django.contrib import admin
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
      User, related_name="posts", 
      on_delete=models.DO_NOTHING,
      blank = True,
      null = True   
		)
    title = models.CharField(max_length = 192, null = True, blank = True)
    sub_title = models.CharField(max_length = 192, null = True, blank = True)
    body = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default = timezone.now)
    likes = models.IntegerField(default = 0)
    unlikes = models.IntegerField(default = 0)