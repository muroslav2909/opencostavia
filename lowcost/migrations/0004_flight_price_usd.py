# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lowcost', '0003_flight_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price_usd',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10),
        ),
    ]
