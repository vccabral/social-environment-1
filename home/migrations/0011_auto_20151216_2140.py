# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20151216_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REPORTING_YEAR',
            field=models.IntegerField(),
        ),
    ]
