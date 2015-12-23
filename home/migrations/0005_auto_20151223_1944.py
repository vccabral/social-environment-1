# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20151223_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Longitude',
            field=models.DecimalField(max_digits=12, decimal_places=8),
        ),
    ]
