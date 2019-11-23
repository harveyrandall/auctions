from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from decimal import Decimal
import datetime

# Helper functions
def default_end_time():
    return datetime.datetime.now() + datetime.timedelta(days=1)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False)
    date_of_birth = models.DateField(blank=False, null=True)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=False, decimal_places=2, max_digits=12)
    bid_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-bid_time']

class Item(models.Model):
    class Meta:
        ordering = ['-posted_time']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=255, blank=False, default="New Item")
    item_description = models.TextField("item description", blank=True)
    item_image = models.ImageField(upload_to="items", height_field=None, width_field=None)
    starting_price = models.DecimalField(decimal_places=2, max_digits=12, default=Decimal('0.01'))
    posted_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(blank=False, default=default_end_time)

    @property
    def item_ended(self):
        return self.end_time.replace(tzinfo=None) < datetime.datetime.now()

    def clean(self):
        if self.end_time.replace(tzinfo=None) < datetime.datetime.now():
            raise ValidationError({
                'end_time': "Auction end time cannot be in the past."
            })