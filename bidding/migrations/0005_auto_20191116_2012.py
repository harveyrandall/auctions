# Generated by Django 2.2.7 on 2019-11-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0004_auto_20191116_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
