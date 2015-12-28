# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from home.baseimport import create_air_quality_database

def create_air_quality_database_1999(apps, schema_editor):
	create_air_quality_database(apps, schema_editor, 1999)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20151228_1931'),
    ]

    operations = [
    	migrations.RunPython(create_air_quality_database_1999),
    ]
