import os
from django.db import models
from django.contrib.auth.models import User



def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.name + os.path.splitext(filename)[1])

class Flowers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=30)
    picture = models.ImageField(upload_to=avatar_upload_to)
# Create your models here.

class Flower_user(models.Model):
    flower_id = models.ForeignKey(Flowers, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

