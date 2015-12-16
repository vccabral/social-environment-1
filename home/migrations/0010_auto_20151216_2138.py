# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20151216_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Year',
            field=models.IntegerField(max_length=1000, blank=True),
        ),
    ]
