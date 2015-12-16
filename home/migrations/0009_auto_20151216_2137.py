# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20151214_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REPORTING_YEAR',
            field=models.IntegerField(max_length=1000, blank=True),
        ),
    ]
