from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    normalized_email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)

class Bid(models.Model):
    amount = models.IntegerField(blank=False)
    TOB = models.DateTimeField(blank = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE )

class Item(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    itemName = models.CharField(max_length = 20)
    description = models.TextField("item description")
    itemImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    startingPrice = models.IntegerField(default = 0)
    bidPrice = models.ForeignKey(Bid, on_delete = models.CASCADE)
