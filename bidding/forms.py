from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import User, Item, Bid
import datetime, time

CURRENT_YEAR = datetime.date.today().year
YEARS = list(range(CURRENT_YEAR - 100, CURRENT_YEAR+1))

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    format = "%H:%M"

class RegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(
        initial=datetime.date.today(),
        widget=DateInput,
        required=True,
        label="Date of birth"
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'date_of_birth')

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'item_image', 'starting_price', 'end_time')
        widgets = {
            'item_image': forms.ClearableFileInput(),
            'end_time': forms.DateTimeInput(
                format="%Y-%m-%d %H:%M",
                attrs={
                    'placeholder': 'YYYY-MM-DD hh:mm'
                })
        }