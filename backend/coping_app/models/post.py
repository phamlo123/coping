from django.db import models
from .user import CustomUser

class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    #TODO: take care of tags
    tags = models.CharField(max_length=10)


