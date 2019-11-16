from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import User, Item, Bid
import datetime

CURRENT_YEAR = datetime.date.today().year
YEARS = list(range(CURRENT_YEAR - 100, CURRENT_YEAR+1))

class DateInput(forms.DateInput):
    input_type = 'date'

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