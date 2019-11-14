from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
import datetime

# Helper functions
def default_end_time():
    return datetime.datetime.now() + datetime.timedelta(days=1)


# Create your models here.
class User(AbstractUser):
    dob = models.DateField(blank=False, null=True)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=False, decimal_places=2, max_digits=12)
    bid_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-bid_time']

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.ForeignKey(Bid, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, blank=False, default="New Item")
    item_description = models.TextField("item description", blank=True)
    item_image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    starting_price = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0.00'))
    posted_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank=False, default=default_end_time)

    class Meta:
        ordering = ['-posted_time']