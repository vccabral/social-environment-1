# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_airqualitydatapoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Address',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Arithmetic_Mean',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Arithmetic_Standard_Dev',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='CBSA_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Certification_Indicator',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='City_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Completeness_Indicator',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='County_Code',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='County_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Date_of_Last_Change',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Datum',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Event_Type',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Exceptional_Data_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Latitude',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Local_Site_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Longitude',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Method_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Metric_Used',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Null_Data_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Num_Obs_Below_MDL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Observation_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Observation_Percent',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='POC',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Parameter_Code',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Parameter_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Pollutant_Standard',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Primary_Exceedance_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Required_Day_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Sample_Duration',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Secondary_Exceedance_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Site_Num',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='State_Code',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='State_Name',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Units_of_Measure',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Valid_Day_Count',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='Year',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='fivezeroth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='fourthth_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='fourthth_Max_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='nineeightth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='ninefiveth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='ninenineth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='ninezeroth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='onest_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='onest_Max_Non_Overlapping_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='onest_Max_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='onest_NO_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='onezeroth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='sevenfiveth_Percentile',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='threerd_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='threerd_Max_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='twod_Max_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='twond_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='twond_Max_Non_Overlapping_Value',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='airqualitydatapoint',
            name='twond_NO_Max_DateTime',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ANCILLARY_OR_OTHER_USE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ASSIGNED_FED_FACILITY_FLAG',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_AN_ARTICLE_COMPONENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_BYPRODUCT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_CHEMICAL_PROCESSING_AID',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_FORMULATION_COMPONENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_MANUFACTURED_IMPURITY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_MANUFACTURING_AID',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_PROCESS_IMPURITY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='AS_A_REACTANT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='CAS_NUMBER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='CERTIFYING_OFFICIALS_SIGNATURE_INDICATOR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='CHEMICAL_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='CLASSIFICATION',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DATE_SIGNED',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DB_NR_A',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DB_NR_B',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_1',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_10',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_11',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_12',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_13',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_14',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_15',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_16',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_17',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_4',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_5',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_6',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_7',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_8',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DIOXIN_DISTRIBUTION_9',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_A_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_A_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_A_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_A_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_A_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_B_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_B_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_B_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_B_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_B_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_C_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_C_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_C_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_C_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_C_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_D_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_D_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_D_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_D_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_D_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_E_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_E_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_E_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_E_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_E_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_F_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_F_PERCENT_FROM_STORMWATER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_F_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_F_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DISCHARGES_TO_STREAM_F_STREAM_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='DOCUMENT_CONTROL_NUMBER',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ENERGY_RECOVERY_ONSITE_CURRENT_YEAR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ENTIRE_FACILITY_IND',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_BIA_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_BIA_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_CITY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_COUNTY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_STATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_STREET',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FACILITY_ZIP_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FEDERAL_FACILITY_IND',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FORM_TYPE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='FUGITIVE_OR_NON_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='GOCO_FACILITY_IND',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='IMPORT_THE_CHEMICAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LANDFILLS_DISPOSAL_SURFACE_IMPOUNDMENTS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LAND_TREATMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LAND_TRTMT_APPL_FARMING_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LAND_TRTMT_APPL_FARMING_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LAND_TRTMT_APPL_FARMING_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LATITUDE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='LONGITUDE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_CITY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_PROVINCE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_STATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_STREET',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAILING_ZIP_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='MAXIMUM_AMOUNT_ONSITE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='METAL_INDICATOR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_CODE_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_CODE_3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_CODE_4',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_CODE_5',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_CODE_6',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAICS_ORIGIN',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NAME_OF_CERTIFYING_OFFICIAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NPDES_NR_A',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='NPDES_NR_B',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_ENERGY_RECOVERY_METHOD_1',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_ENERGY_RECOVERY_METHOD_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_ENERGY_RECOVERY_METHOD_3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_ENERGY_RECOVERY_METHOD_4',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_1',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_10',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_4',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_5',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_6',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_7',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_8',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_RECYCLING_PROCESSES_METHOD_9',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='ON_SITE_USE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_DISPOSAL_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_DISPOSAL_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_DISPOSAL_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_LANDFILLS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_LANDFILLS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_LANDFILLS_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_LANDFILLS_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_LAND_DISPOSAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_OFF_SITE_MANAGEMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_ON_SITE_WASTE_MANAGEMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_SURFACE_IMPOUNDMENTS_M67',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_SURFACE_IMPOUNDMENT_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='OTHER_SURFACE_IMPOUNDMENT_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PARENT_COMPANY_DB_NR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PARENT_COMPANY_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PARTIAL_FACILITY_IND',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='POTWS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='POTWS_TOTAL_TRANSFERS_METALS_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PRIMARY_NAICS_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PRIMARY_SIC_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PRODUCE_THE_CHEMICAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PUBLIC_CONTACT_EMAIL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PUBLIC_CONTACT_NAME',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='PUBLIC_CONTACT_PHONE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='QUANTITY_RECYCLED_ONSITE_CURRENT_YEAR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='QUANTITY_TREATED_ONSITE_CURRENT_YEAR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_C_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_C_SURFACE_IMPOUNDMENT_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_C_SURFACE_IMPOUNDMENT_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_NR_A',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_NR_B',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_SUBTITLE_C_LANDFILLS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_SUBTITLE_C_LANDFILLS_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_SUBTITLE_C_LANDFILLS_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_SUBTITLE_C_LANDFILSS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='RCRA_SUBTITLE_C_SURFACE_IMPOUNDMENTS_M66',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REPACKAGING',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REPORTING_YEAR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REVISION_CODE_1',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='REVISION_CODE_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SALE_OR_DISTRIBUTION',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SANITIZED_INDICATOR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SIC_CODE_2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SIC_CODE_3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SIC_CODE_4',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SIC_CODE_5',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SIC_CODE_6',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SOLIDIFICATION_STABILIZATION_METALS_AND_METAL_COMPOUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='STACK_AIR_EMISSIONS_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='STACK_AIR_EMISSIONS_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='STACK_OR_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='STORAGE_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SURFACE_IMPOUNDMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SURFACE_IMPOUNDMENT_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='SURFACE_IMPOUNDMENT_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TITLE_OF_CERTIFYING_OFFICIAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_AIR_EMISSIONS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_A',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_B',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_C',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_D',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_E',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_DISCHARGES_TO_STREAM_F',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_FUGITIVE_AIR_EMISSIONS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_LAND_TREATMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_NUMBER_OF_RECEIVING_STREAMS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_ON_SITE_LAND_RELEASES',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_OTHER_DISPOSAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_OTHER_ON_SITE_LAND_RELEASES',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_OTHER_SURFACE_IMPOUNDMENTS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_RCRA_C_SURFACE_IMPOUNDMENTS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_RCRA_SUBTITLE_C_LANDFILLS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_STACK_AIR_EMISSIONS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_SURFACE_IMPOUNDMENTS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_SURFACE_WATER_DISCHARGE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_TRANSFERRED_OFF_SITE_FOR_FURTHER_WASTE_MANAGEMENT',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_TRANSFERRED_OFF_SITE_TO_DISPOSAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_UGRND_INJ_ONSITE_TO_CL_I_WELLS_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TOTAL_UNDERGROUND_INJECTION',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRADE_SECRET_INDICATOR',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_ENERGY_RECOVERY_M56_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_ENERGY_RECOVERY_M92_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_POTWS_METALS_AND_METAL_COMPOUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_POTWS_NON_METALS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_RECYCLING_M20_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_RECYCLING_M24_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_RECYCLING_M26_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_RECYCLING_M28_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_RECYCLING_M93_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M40_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M50_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M54_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M61_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M69_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_TREATMENT_M95_ONLY',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRANSFERS_TO_WASTE_BROKER_FOR_DISPOSAL',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='TRIFID',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UGRND_INJ_ONSITE_TO_CL_I_WELLS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_POUNDS',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_RANGE_CODE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UIC_NR_A',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UIC_NR_B',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNDERGROUND_INJECTION',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNDERGROUND_INJECTION_TO_CLASS_II_V_WELLS_M82',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNDERGROUND_INJECTION_TO_CLASS_I_WELLS_M81',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNGRND_INJ_ONSITE_TO_CL_II_V_WELLS_BASIS_OF_ESTIMATE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNIT_OF_MEASURE',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='UNKNOWN',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='toxicdatapoint',
            name='WASTEWATER_TREATMENT_EXCLUDING_POTWS',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
