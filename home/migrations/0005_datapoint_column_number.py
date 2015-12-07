# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_datapoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='column_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
