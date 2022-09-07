# Generated by Django 3.2.5 on 2022-08-08 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autionapp', '0003_remove_buyer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='highest_bidder_id',
        ),
        migrations.CreateModel(
            name='NewTrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction_end_time', models.TimeField()),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autionapp.house')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
