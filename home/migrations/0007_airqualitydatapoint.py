# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_toxicdatapoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirQualityDataPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('State_Code', models.CharField(max_length=1000)),
                ('County_Code', models.CharField(max_length=1000)),
                ('Site_Num', models.CharField(max_length=1000)),
                ('Parameter_Code', models.CharField(max_length=1000)),
                ('POC', models.CharField(max_length=1000)),
                ('Latitude', models.CharField(max_length=1000)),
                ('Longitude', models.CharField(max_length=1000)),
                ('Datum', models.CharField(max_length=1000)),
                ('Parameter_Name', models.CharField(max_length=1000)),
                ('Sample_Duration', models.CharField(max_length=1000)),
                ('Pollutant_Standard', models.CharField(max_length=1000)),
                ('Metric_Used', models.CharField(max_length=1000)),
                ('Method_Name', models.CharField(max_length=1000)),
                ('Year', models.CharField(max_length=1000)),
                ('Units_of_Measure', models.CharField(max_length=1000)),
                ('Event_Type', models.CharField(max_length=1000)),
                ('Observation_Count', models.CharField(max_length=1000)),
                ('Observation_Percent', models.CharField(max_length=1000)),
                ('Completeness_Indicator', models.CharField(max_length=1000)),
                ('Valid_Day_Count', models.CharField(max_length=1000)),
                ('Required_Day_Count', models.CharField(max_length=1000)),
                ('Exceptional_Data_Count', models.CharField(max_length=1000)),
                ('Null_Data_Count', models.CharField(max_length=1000)),
                ('Primary_Exceedance_Count', models.CharField(max_length=1000)),
                ('Secondary_Exceedance_Count', models.CharField(max_length=1000)),
                ('Certification_Indicator', models.CharField(max_length=1000)),
                ('Num_Obs_Below_MDL', models.CharField(max_length=1000)),
                ('Arithmetic_Mean', models.CharField(max_length=1000)),
                ('Arithmetic_Standard_Dev', models.CharField(max_length=1000)),
                ('onest_Max_Value', models.CharField(max_length=1000)),
                ('onest_Max_DateTime', models.CharField(max_length=1000)),
                ('twod_Max_Value', models.CharField(max_length=1000)),
                ('twond_Max_DateTime', models.CharField(max_length=1000)),
                ('threerd_Max_Value', models.CharField(max_length=1000)),
                ('threerd_Max_DateTime', models.CharField(max_length=1000)),
                ('fourthth_Max_Value', models.CharField(max_length=1000)),
                ('fourthth_Max_DateTime', models.CharField(max_length=1000)),
                ('onest_Max_Non_Overlapping_Value', models.CharField(max_length=1000)),
                ('onest_NO_Max_DateTime', models.CharField(max_length=1000)),
                ('twond_Max_Non_Overlapping_Value', models.CharField(max_length=1000)),
                ('twond_NO_Max_DateTime', models.CharField(max_length=1000)),
                ('ninenineth_Percentile', models.CharField(max_length=1000)),
                ('nineeightth_Percentile', models.CharField(max_length=1000)),
                ('ninefiveth_Percentile', models.CharField(max_length=1000)),
                ('ninezeroth_Percentile', models.CharField(max_length=1000)),
                ('sevenfiveth_Percentile', models.CharField(max_length=1000)),
                ('fivezeroth_Percentile', models.CharField(max_length=1000)),
                ('onezeroth_Percentile', models.CharField(max_length=1000)),
                ('Local_Site_Name', models.CharField(max_length=1000)),
                ('Address', models.CharField(max_length=1000)),
                ('State_Name', models.CharField(max_length=1000)),
                ('County_Name', models.CharField(max_length=1000)),
                ('City_Name', models.CharField(max_length=1000)),
                ('CBSA_Name', models.CharField(max_length=1000)),
                ('Date_of_Last_Change', models.CharField(max_length=1000)),
            ],
        ),
    ]
