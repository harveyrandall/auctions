# Generated by Django 2.2.7 on 2019-11-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0003_auto_20191114_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
