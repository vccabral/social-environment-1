# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core import management

def create_air_quality_database(apps, schema_editor):

    AirQualityDataPoint = apps.get_model("home", "AirQualityDataPoint")
    ToxicDataPoint = apps.get_model("home", "ToxicDataPoint")

    if AirQualityDataPoint.objects.all().count() == 0:
    	for i in range(2010, 2014):
			management.call_command('import_raw_data', str(i), str(i), str(100000), '--air', '--toxic', '--redo')


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailusers','0003_add_verbose_names')
    ]

    operations = [
    	migrations.RunPython(create_air_quality_database),
    ]
