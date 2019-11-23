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

class Item(models.Model):
    class Meta:
        ordering = ['-posted_time']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Bid(models.Model):
    class Meta:
        ordering = ['-bid_time']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=True)
    amount = models.DecimalField(blank=False, decimal_places=2, max_digits=21, default=Decimal('0.01'))
    bid_time = models.DateTimeField(auto_now=True)

    @staticmethod
    def highest_bid(item):
        bids = Bid.objects.filter(item=item)
        if bids:
            return bids.aggregate(models.Max('amount')).get('amount__max')
        else:
            return None

    def clean(self):
        try:
            if self.amount < self.highest_bid(self.item.pk):
                raise ValidationError({
                    'amount': "Bid must be higher than the previous one."
                })
        except TypeError:
            pass

        if self.item.item_ended:
            raise ValidationError({
                'item': "The auction for this item has ended. You can no longer bid on it."
            })
