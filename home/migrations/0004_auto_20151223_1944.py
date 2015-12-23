# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151223_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Latitude',
            field=models.DecimalField(max_digits=12, decimal_places=8),
        ),
    ]
