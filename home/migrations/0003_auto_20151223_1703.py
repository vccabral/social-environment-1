# -*- coding: utf-8 -*-
from django.db import migrations, models, connection
from django.core import management
from django.conf import settings

import os.path
import zipfile
import urllib
import sys, traceback
import csv


def encode_for_database(local_string):
    if local_string.startswith("\"") and local_string.endswith("\""):
        local_string = local_string[1:-1]
    elif local_string.startswith("\"") and local_string.endswith("\"\n"):
        local_string = local_string[1:-2]
    return unicode(local_string, errors='ignore') 


def empty_air_quality_database(apps, schema_editor):

    AirQualityDataPoint = apps.get_model("home", "AirQualityDataPoint")
    ToxicDataPoint = apps.get_model("home", "ToxicDataPoint")
    RawDataMap = apps.get_model("home", "RawDataMap")

    years_range = range(1987, 2015)

    for year in years_range:
        while ToxicDataPoint.objects.all().exists():
            ToxicDataPoint.objects.filter(REPORTING_YEAR=year)[:max_insert_quantity].delete()
        while AirQualityDataPoint.objects.all().exists():
            AirQualityDataPoint.objects.filter(Year=year)[:max_insert_quantity].delete()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailusers','0003_add_verbose_names')
    ]

    operations = [
    	migrations.RunPython(empty_air_quality_database),
    ]
