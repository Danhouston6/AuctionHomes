# Generated by Django 3.2.5 on 2022-08-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autionapp', '0009_auto_20220810_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='list_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='max_bid_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='starting_price',
            field=models.IntegerField(),
        ),
    ]