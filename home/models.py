from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    pass


class RawDataMap(models.Model):
	import_id = models.CharField(max_length=100)
	identifier = models.CharField(max_length=200)

class DataPoint(models.Model):
	data_set = models.CharField(max_length=200)
	column_value = models.CharField(max_length=200)
	point_value = models.CharField(max_length=500)