# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rawdatamap'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_set', models.CharField(max_length=200)),
                ('column_value', models.CharField(max_length=200)),
                ('point_value', models.CharField(max_length=500)),
            ],
        ),
    ]
