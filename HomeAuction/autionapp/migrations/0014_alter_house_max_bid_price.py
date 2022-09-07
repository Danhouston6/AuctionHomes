# Generated by Django 3.2.5 on 2022-09-03 06:18

import autionapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autionapp', '0013_alter_house_max_bid_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='max_bid_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, validators=[autionapp.models.check_if_max_bid]),
        ),
    ]
