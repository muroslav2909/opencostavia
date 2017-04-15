# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lowcost', '0002_add_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='currency',
            field=models.ForeignKey(default=None, blank=True, to='lowcost.Currency', null=True),
        ),
    ]
