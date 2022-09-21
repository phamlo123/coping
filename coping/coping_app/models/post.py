from django.db import models
from .user import User

class Post(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    content = models.CharField(max_length=1000)
    #TODO: take care of tags
    tags = models.CharField(max_length=10)


