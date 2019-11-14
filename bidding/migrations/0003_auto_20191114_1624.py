# Generated by Django 2.2.7 on 2019-11-14 16:24

from decimal import Decimal
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_auto_20191113_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-bid_time']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-posted_time']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='bidPrice',
            new_name='bid_price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itemImage',
            new_name='item_image',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='tob',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemName',
        ),
        migrations.RemoveField(
            model_name='item',
            name='startingPrice',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='normalized_email',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, verbose_name='item description'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='New Item', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='posted_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='item',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
