from django.core.management.base import BaseCommand, CommandError
from django.db import connection
import os.path
import zipfile
import urllib
from home.models import RawDataMap, DataPoint, ToxicDataPoint, AirQualityDataPoint

def encode_for_database(local_string):
    if local_string.startswith("\"") and local_string.endswit("\""):
        local_string = local_string[1:-1]
    return unicode(local_string, errors='ignore') 


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        print("import raw data")
        temp_dir = "/tmp/"

        connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        DataPoint.objects.all().delete()
        ToxicDataPoint.objects.all().delete()
        AirQualityDataPoint.objects.all().delete()

        for year in range(1987, 2014):
            filename = "US_"+str(year)+"_v13.zip"
            download_url = "http://www3.epa.gov/tri/"+filename
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"US_1_"+str(year)+"_v13.txt"

            if not os.path.isfile(file_path):
                urllib.urlretrieve(download_url, file_path)
                print("downloaded: "+file_path)

        for year in range(1987, 2014):
            filename = "US_"+str(year)+"_v13.zip"
            download_url = "http://www3.epa.gov/tri/"+filename
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"US_1_"+str(year)+"_v13.txt"

            if os.path.isfile(file_path):
                with zipfile.ZipFile(file_path, "r") as z:
                    z.extractall(tmp_path)

        for year in range(1990, 2016):
            filename = "annual_all_"+str(year)+".zip"
            download_url = "http://aqsdr1.epa.gov/aqsweb/aqstmp/airdata/"+filename  
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"annual_all_"+str(year)+".csv"

            if not os.path.isfile(file_path):
                urllib.urlretrieve(download_url, file_path)
                print("downloaded: "+file_path)

        for year in range(1990, 2016):
            filename = "annual_all_"+str(year)+".zip"
            download_url = "http://aqsdr1.epa.gov/aqsweb/aqstmp/airdata/"+filename  
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"annual_all_"+str(year)+".csv"

            if os.path.isfile(file_path):
                with zipfile.ZipFile(file_path, "r") as z:
                    z.extractall(tmp_path)


        for year in range(1987, 2014):
            filename = "US_"+str(year)+"_v13.zip"
            download_url = "http://www3.epa.gov/tri/"+filename
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"US_1_"+str(year)+"_v13.txt"

            print("working on ", unzipped_file_path)

            if os.path.isfile(unzipped_file_path):
                with open(unzipped_file_path, 'r') as f:
                    is_first_line = True
                    index_to_column = {}
                    counter = 0
                    for line in f: 
                        counter = counter + 1
                        if counter % 1000 == 0:
                            print(counter)
                        columns = line.split("\t")
                        if is_first_line:
                            for column_index, column in enumerate(columns):
                                index_to_column[column_index] = column
                                if not RawDataMap.objects.filter(import_id="toxic release", identifier=column).exists():
                                    RawDataMap(import_id="toxic release", identifier=column).save()
                            is_first_line = False
                        else:
                            try:
                                ToxicDataPoint(
                                    FORM_TYPE = encode_for_database(columns[0]),
                                    REPORTING_YEAR = encode_for_database(columns[1]),
                                    TRADE_SECRET_INDICATOR = encode_for_database(columns[2]),
                                    SANITIZED_INDICATOR = encode_for_database(columns[3]),
                                    TITLE_OF_CERTIFYING_OFFICIAL = encode_for_database(columns[4]),
                                    NAME_OF_CERTIFYING_OFFICIAL = encode_for_database(columns[5]),
                                    CERTIFYING_OFFICIALS_SIGNATURE_INDICATOR = encode_for_database(columns[6]),
                                    DATE_SIGNED = encode_for_database(columns[7]),
                                    TRIFID = encode_for_database(columns[8]),
                                    FACILITY_NAME = encode_for_database(columns[9]),
                                    FACILITY_STREET = encode_for_database(columns[10]),
                                    FACILITY_CITY = encode_for_database(columns[11]),
                                    FACILITY_COUNTY = encode_for_database(columns[12]),
                                    FACILITY_STATE = encode_for_database(columns[13]),
                                    FACILITY_ZIP_CODE = encode_for_database(columns[14]),
                                    FACILITY_BIA_CODE = encode_for_database(columns[15]),
                                    FACILITY_BIA_NAME = encode_for_database(columns[16]),
                                    MAILING_NAME = encode_for_database(columns[17]),
                                    MAILING_STREET = encode_for_database(columns[18]),
                                    MAILING_CITY = encode_for_database(columns[19]),
                                    MAILING_STATE = encode_for_database(columns[20]),
                                    MAILING_PROVINCE = encode_for_database(columns[21]),
                                    MAILING_ZIP_CODE = encode_for_database(columns[22]),
                                    ENTIRE_FACILITY_IND = encode_for_database(columns[23]),
                                    PARTIAL_FACILITY_IND = encode_for_database(columns[24]),
                                    FEDERAL_FACILITY_IND = encode_for_database(columns[25]),
                                    GOCO_FACILITY_IND = encode_for_database(columns[26]),
                                    PUBLIC_CONTACT_NAME = encode_for_database(columns[27]),
                                    PUBLIC_CONTACT_PHONE = encode_for_database(columns[28]),
                                    PRIMARY_SIC_CODE = encode_for_database(columns[29]),
                                    SIC_CODE_2 = encode_for_database(columns[30]),
                                    SIC_CODE_3 = encode_for_database(columns[31]),
                                    SIC_CODE_4 = encode_for_database(columns[32]),
                                    SIC_CODE_5 = encode_for_database(columns[33]),
                                    SIC_CODE_6 = encode_for_database(columns[34]),
                                    NAICS_ORIGIN = encode_for_database(columns[35]),
                                    PRIMARY_NAICS_CODE = encode_for_database(columns[36]),
                                    NAICS_CODE_2 = encode_for_database(columns[37]),
                                    NAICS_CODE_3 = encode_for_database(columns[38]),
                                    NAICS_CODE_4 = encode_for_database(columns[39]),
                                    NAICS_CODE_5 = encode_for_database(columns[40]),
                                    NAICS_CODE_6 = encode_for_database(columns[41]),
                                    LATITUDE = encode_for_database(columns[42]),
                                    LONGITUDE = encode_for_database(columns[43]),
                                    DB_NR_A = encode_for_database(columns[44]),
                                    DB_NR_B = encode_for_database(columns[45]),
                                    RCRA_NR_A = encode_for_database(columns[46]),
                                    RCRA_NR_B = encode_for_database(columns[47]),
                                    NPDES_NR_A = encode_for_database(columns[48]),
                                    NPDES_NR_B = encode_for_database(columns[49]),
                                    UIC_NR_A = encode_for_database(columns[50]),
                                    UIC_NR_B = encode_for_database(columns[51]),
                                    PARENT_COMPANY_NAME = encode_for_database(columns[52]),
                                    PARENT_COMPANY_DB_NR = encode_for_database(columns[53]),
                                    DOCUMENT_CONTROL_NUMBER = encode_for_database(columns[54]),
                                    CAS_NUMBER = encode_for_database(columns[55]),
                                    CHEMICAL_NAME = encode_for_database(columns[56]),
                                    CLASSIFICATION = encode_for_database(columns[57]),
                                    UNIT_OF_MEASURE = encode_for_database(columns[58]),
                                    DIOXIN_DISTRIBUTION_1 = encode_for_database(columns[59]),
                                    DIOXIN_DISTRIBUTION_2 = encode_for_database(columns[60]),
                                    DIOXIN_DISTRIBUTION_3 = encode_for_database(columns[61]),
                                    DIOXIN_DISTRIBUTION_4 = encode_for_database(columns[62]),
                                    DIOXIN_DISTRIBUTION_5 = encode_for_database(columns[63]),
                                    DIOXIN_DISTRIBUTION_6 = encode_for_database(columns[64]),
                                    DIOXIN_DISTRIBUTION_7 = encode_for_database(columns[65]),
                                    DIOXIN_DISTRIBUTION_8 = encode_for_database(columns[66]),
                                    DIOXIN_DISTRIBUTION_9 = encode_for_database(columns[67]),
                                    DIOXIN_DISTRIBUTION_10 = encode_for_database(columns[68]),
                                    DIOXIN_DISTRIBUTION_11 = encode_for_database(columns[69]),
                                    DIOXIN_DISTRIBUTION_12 = encode_for_database(columns[70]),
                                    DIOXIN_DISTRIBUTION_13 = encode_for_database(columns[71]),
                                    DIOXIN_DISTRIBUTION_14 = encode_for_database(columns[72]),
                                    DIOXIN_DISTRIBUTION_15 = encode_for_database(columns[73]),
                                    DIOXIN_DISTRIBUTION_16 = encode_for_database(columns[74]),
                                    DIOXIN_DISTRIBUTION_17 = encode_for_database(columns[75]),
                                    PRODUCE_THE_CHEMICAL = encode_for_database(columns[76]),
                                    IMPORT_THE_CHEMICAL = encode_for_database(columns[77]),
                                    ON_SITE_USE = encode_for_database(columns[78]),
                                    SALE_OR_DISTRIBUTION = encode_for_database(columns[79]),
                                    AS_A_BYPRODUCT = encode_for_database(columns[80]),
                                    AS_A_MANUFACTURED_IMPURITY = encode_for_database(columns[81]),
                                    AS_A_REACTANT = encode_for_database(columns[82]),
                                    AS_A_FORMULATION_COMPONENT = encode_for_database(columns[83]),
                                    AS_AN_ARTICLE_COMPONENT = encode_for_database(columns[84]),
                                    REPACKAGING = encode_for_database(columns[85]),
                                    AS_A_PROCESS_IMPURITY = encode_for_database(columns[86]),
                                    AS_A_CHEMICAL_PROCESSING_AID = encode_for_database(columns[87]),
                                    AS_A_MANUFACTURING_AID = encode_for_database(columns[88]),
                                    ANCILLARY_OR_OTHER_USE = encode_for_database(columns[89]),
                                    MAXIMUM_AMOUNT_ONSITE = encode_for_database(columns[90]),
                                    FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_POUNDS = encode_for_database(columns[91]),
                                    FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_RANGE_CODE = encode_for_database(columns[92]),
                                    TOTAL_FUGITIVE_AIR_EMISSIONS = encode_for_database(columns[93]),
                                    FUGITIVE_OR_NON_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE = encode_for_database(columns[94]),
                                    STACK_AIR_EMISSIONS_RELEASE_POUNDS = encode_for_database(columns[95]),
                                    STACK_AIR_EMISSIONS_RELEASE_RANGE_CODE = encode_for_database(columns[96]),
                                    TOTAL_STACK_AIR_EMISSIONS = encode_for_database(columns[97]),
                                    STACK_OR_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE = encode_for_database(columns[98]),
                                    TOTAL_AIR_EMISSIONS = encode_for_database(columns[99]),
                                    DISCHARGES_TO_STREAM_A_STREAM_NAME = encode_for_database(columns[100]),
                                    DISCHARGES_TO_STREAM_A_RELEASE_POUNDS = encode_for_database(columns[101]),
                                    DISCHARGES_TO_STREAM_A_RELEASE_RANGE_CODE = encode_for_database(columns[102]),
                                    TOTAL_DISCHARGES_TO_STREAM_A = encode_for_database(columns[103]),
                                    DISCHARGES_TO_STREAM_A_BASIS_OF_ESTIMATE = encode_for_database(columns[104]),
                                    DISCHARGES_TO_STREAM_A_PERCENT_FROM_STORMWATER = encode_for_database(columns[105]),
                                    DISCHARGES_TO_STREAM_B_STREAM_NAME = encode_for_database(columns[106]),
                                    DISCHARGES_TO_STREAM_B_RELEASE_POUNDS = encode_for_database(columns[107]),
                                    DISCHARGES_TO_STREAM_B_RELEASE_RANGE_CODE = encode_for_database(columns[108]),
                                    TOTAL_DISCHARGES_TO_STREAM_B = encode_for_database(columns[109]),
                                    DISCHARGES_TO_STREAM_B_BASIS_OF_ESTIMATE = encode_for_database(columns[110]),
                                    DISCHARGES_TO_STREAM_B_PERCENT_FROM_STORMWATER = encode_for_database(columns[111]),
                                    DISCHARGES_TO_STREAM_C_STREAM_NAME = encode_for_database(columns[112]),
                                    DISCHARGES_TO_STREAM_C_RELEASE_POUNDS = encode_for_database(columns[113]),
                                    DISCHARGES_TO_STREAM_C_RELEASE_RANGE_CODE = encode_for_database(columns[114]),
                                    TOTAL_DISCHARGES_TO_STREAM_C = encode_for_database(columns[115]),
                                    DISCHARGES_TO_STREAM_C_BASIS_OF_ESTIMATE = encode_for_database(columns[116]),
                                    DISCHARGES_TO_STREAM_C_PERCENT_FROM_STORMWATER = encode_for_database(columns[117]),
                                    DISCHARGES_TO_STREAM_D_STREAM_NAME = encode_for_database(columns[118]),
                                    DISCHARGES_TO_STREAM_D_RELEASE_POUNDS = encode_for_database(columns[119]),
                                    DISCHARGES_TO_STREAM_D_RELEASE_RANGE_CODE = encode_for_database(columns[120]),
                                    TOTAL_DISCHARGES_TO_STREAM_D = encode_for_database(columns[121]),
                                    DISCHARGES_TO_STREAM_D_BASIS_OF_ESTIMATE = encode_for_database(columns[122]),
                                    DISCHARGES_TO_STREAM_D_PERCENT_FROM_STORMWATER = encode_for_database(columns[123]),
                                    DISCHARGES_TO_STREAM_E_STREAM_NAME = encode_for_database(columns[124]),
                                    DISCHARGES_TO_STREAM_E_RELEASE_POUNDS = encode_for_database(columns[125]),
                                    DISCHARGES_TO_STREAM_E_RELEASE_RANGE_CODE = encode_for_database(columns[126]),
                                    TOTAL_DISCHARGES_TO_STREAM_E = encode_for_database(columns[127]),
                                    DISCHARGES_TO_STREAM_E_BASIS_OF_ESTIMATE = encode_for_database(columns[128]),
                                    DISCHARGES_TO_STREAM_E_PERCENT_FROM_STORMWATER = encode_for_database(columns[129]),
                                    DISCHARGES_TO_STREAM_F_STREAM_NAME = encode_for_database(columns[130]),
                                    DISCHARGES_TO_STREAM_F_RELEASE_POUNDS = encode_for_database(columns[131]),
                                    DISCHARGES_TO_STREAM_F_RELEASE_RANGE_CODE = encode_for_database(columns[132]),
                                    TOTAL_DISCHARGES_TO_STREAM_F = encode_for_database(columns[133]),
                                    DISCHARGES_TO_STREAM_F_BASIS_OF_ESTIMATE = encode_for_database(columns[134]),
                                    DISCHARGES_TO_STREAM_F_PERCENT_FROM_STORMWATER = encode_for_database(columns[135]),
                                    TOTAL_NUMBER_OF_RECEIVING_STREAMS = encode_for_database(columns[136]),
                                    TOTAL_SURFACE_WATER_DISCHARGE = encode_for_database(columns[137]),
                                    UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_POUNDS = encode_for_database(columns[138]),
                                    UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_RANGE_CODE = encode_for_database(columns[139]),
                                    TOTAL_UGRND_INJ_ONSITE_TO_CL_I_WELLS_POUNDS = encode_for_database(columns[140]),
                                    UGRND_INJ_ONSITE_TO_CL_I_WELLS_BASIS_OF_ESTIMATE = encode_for_database(columns[141]),
                                    UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_POUNDS = encode_for_database(columns[142]),
                                    UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_RANGE_CODE = encode_for_database(columns[143]),
                                    TOTAL_UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_POUNDS = encode_for_database(columns[144]),
                                    UNGRND_INJ_ONSITE_TO_CL_II_V_WELLS_BASIS_OF_ESTIMATE = encode_for_database(columns[145]),
                                    TOTAL_UNDERGROUND_INJECTION = encode_for_database(columns[146]),
                                    RCRA_SUBTITLE_C_LANDFILLS_RELEASE_POUNDS = encode_for_database(columns[147]),
                                    RCRA_SUBTITLE_C_LANDFILLS_RELEASE_RANGE_CODE = encode_for_database(columns[148]),
                                    TOTAL_RCRA_SUBTITLE_C_LANDFILLS = encode_for_database(columns[149]),
                                    RCRA_SUBTITLE_C_LANDFILLS_BASIS_OF_ESTIMATE = encode_for_database(columns[150]),
                                    OTHER_LANDFILLS_RELEASE_POUNDS = encode_for_database(columns[151]),
                                    OTHER_LANDFILLS_RELEASE_RANGE_CODE = encode_for_database(columns[152]),
                                    TOTAL_OTHER_ON_SITE_LAND_RELEASES = encode_for_database(columns[153]),
                                    OTHER_LANDFILLS_BASIS_OF_ESTIMATE = encode_for_database(columns[154]),
                                    LAND_TRTMT_APPL_FARMING_RELEASE_POUNDS = encode_for_database(columns[155]),
                                    LAND_TRTMT_APPL_FARMING_RELEASE_RANGE_CODE = encode_for_database(columns[156]),
                                    TOTAL_LAND_TREATMENT = encode_for_database(columns[157]),
                                    LAND_TRTMT_APPL_FARMING_BASIS_OF_ESTIMATE = encode_for_database(columns[158]),
                                    SURFACE_IMPOUNDMENT_RELEASE_POUNDS = encode_for_database(columns[159]),
                                    SURFACE_IMPOUNDMENT_RANGE_CODE = encode_for_database(columns[160]),
                                    TOTAL_SURFACE_IMPOUNDMENTS = encode_for_database(columns[161]),
                                    SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = encode_for_database(columns[162]),
                                    OTHER_DISPOSAL_RELEASE_POUNDS = encode_for_database(columns[163]),
                                    OTHER_DISPOSAL_RANGE_CODE = encode_for_database(columns[164]),
                                    TOTAL_OTHER_DISPOSAL = encode_for_database(columns[165]),
                                    OTHER_DISPOSAL_BASIS_OF_ESTIMATE = encode_for_database(columns[166]),
                                    TOTAL_ON_SITE_LAND_RELEASES = encode_for_database(columns[167]),
                                    POTWS_TOTAL_TRANSFERS_METALS_ONLY = encode_for_database(columns[168]),
                                    POTWS_BASIS_OF_ESTIMATE = encode_for_database(columns[169]),
                                    STORAGE_ONLY = encode_for_database(columns[170]),
                                    SOLIDIFICATION_STABILIZATION_METALS_AND_METAL_COMPOUNDS = encode_for_database(columns[171]),
                                    WASTEWATER_TREATMENT_EXCLUDING_POTWS = encode_for_database(columns[172]),
                                    TRANSFERS_TO_POTWS_METALS_AND_METAL_COMPOUNDS = encode_for_database(columns[173]),
                                    UNDERGROUND_INJECTION = encode_for_database(columns[174]),
                                    LANDFILLS_DISPOSAL_SURFACE_IMPOUNDMENTS = encode_for_database(columns[175]),
                                    SURFACE_IMPOUNDMENT = encode_for_database(columns[176]),
                                    OTHER_LANDFILLS = encode_for_database(columns[177]),
                                    RCRA_SUBTITLE_C_LANDFILSS = encode_for_database(columns[178]),
                                    LAND_TREATMENT = encode_for_database(columns[179]),
                                    OTHER_LAND_DISPOSAL = encode_for_database(columns[180]),
                                    OTHER_OFF_SITE_MANAGEMENT = encode_for_database(columns[181]),
                                    TRANSFERS_TO_WASTE_BROKER_FOR_DISPOSAL = encode_for_database(columns[182]),
                                    UNKNOWN = encode_for_database(columns[183]),
                                    TOTAL_TRANSFERRED_OFF_SITE_TO_DISPOSAL = encode_for_database(columns[184]),
                                    TRANSFERS_TO_RECYCLING_M20_ONLY = encode_for_database(columns[185]),
                                    TRANSFERS_TO_RECYCLING_M24_ONLY = encode_for_database(columns[186]),
                                    TRANSFERS_TO_RECYCLING_M26_ONLY = encode_for_database(columns[187]),
                                    TRANSFERS_TO_RECYCLING_M28_ONLY = encode_for_database(columns[188]),
                                    TRANSFERS_TO_RECYCLING_M93_ONLY = encode_for_database(columns[189]),
                                    TRANSFERS_TO_ENERGY_RECOVERY_M56_ONLY = encode_for_database(columns[190]),
                                    TRANSFERS_TO_ENERGY_RECOVERY_M92_ONLY = encode_for_database(columns[191]),
                                    TRANSFERS_TO_TREATMENT_M40_ONLY = encode_for_database(columns[192]),
                                    TRANSFERS_TO_TREATMENT_M50_ONLY = encode_for_database(columns[193]),
                                    TRANSFERS_TO_TREATMENT_M54_ONLY = encode_for_database(columns[194]),
                                    TRANSFERS_TO_TREATMENT_M61_ONLY = encode_for_database(columns[195]),
                                    TRANSFERS_TO_TREATMENT_M69_ONLY = encode_for_database(columns[196]),
                                    TRANSFERS_TO_TREATMENT_M95_ONLY = encode_for_database(columns[197]),
                                    TRANSFERS_TO_POTWS_NON_METALS = encode_for_database(columns[198]),
                                    TOTAL_TRANSFERRED_OFF_SITE_FOR_FURTHER_WASTE_MANAGEMENT = encode_for_database(columns[199]),
                                    ENERGY_RECOVERY_ONSITE_CURRENT_YEAR = encode_for_database(columns[200]),
                                    QUANTITY_RECYCLED_ONSITE_CURRENT_YEAR = encode_for_database(columns[201]),
                                    QUANTITY_TREATED_ONSITE_CURRENT_YEAR = encode_for_database(columns[202]),
                                    OTHER_ON_SITE_WASTE_MANAGEMENT = encode_for_database(columns[203]),
                                    ON_SITE_ENERGY_RECOVERY_METHOD_1 = encode_for_database(columns[204]),
                                    ON_SITE_ENERGY_RECOVERY_METHOD_2 = encode_for_database(columns[205]),
                                    ON_SITE_ENERGY_RECOVERY_METHOD_3 = encode_for_database(columns[206]),
                                    ON_SITE_ENERGY_RECOVERY_METHOD_4 = encode_for_database(columns[207]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_1 = encode_for_database(columns[208]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_2 = encode_for_database(columns[209]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_3 = encode_for_database(columns[210]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_4 = encode_for_database(columns[211]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_5 = encode_for_database(columns[212]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_6 = encode_for_database(columns[213]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_7 = encode_for_database(columns[214]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_8 = encode_for_database(columns[215]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_9 = encode_for_database(columns[216]),
                                    ON_SITE_RECYCLING_PROCESSES_METHOD_10 = encode_for_database(columns[217]),
                                    RCRA_C_SURFACE_IMPOUNDMENT_RELEASE_POUNDS = encode_for_database(columns[218]),
                                    RCRA_C_SURFACE_IMPOUNDMENT_RANGE_CODE = encode_for_database(columns[219]),
                                    TOTAL_RCRA_C_SURFACE_IMPOUNDMENTS = encode_for_database(columns[220]),
                                    RCRA_C_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = encode_for_database(columns[221]),
                                    OTHER_SURFACE_IMPOUNDMENT_RELEASE_POUNDS = encode_for_database(columns[222]),
                                    OTHER_SURFACE_IMPOUNDMENT_RANGE_CODE = encode_for_database(columns[223]),
                                    TOTAL_OTHER_SURFACE_IMPOUNDMENTS = encode_for_database(columns[224]),
                                    OTHER_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = encode_for_database(columns[225]),
                                    RCRA_SUBTITLE_C_SURFACE_IMPOUNDMENTS_M66 = encode_for_database(columns[226]),
                                    OTHER_SURFACE_IMPOUNDMENTS_M67 = encode_for_database(columns[227]),
                                    UNDERGROUND_INJECTION_TO_CLASS_I_WELLS_M81 = encode_for_database(columns[228]),
                                    UNDERGROUND_INJECTION_TO_CLASS_II_V_WELLS_M82 = encode_for_database(columns[229]),
                                    ASSIGNED_FED_FACILITY_FLAG = encode_for_database(columns[230]),
                                    PUBLIC_CONTACT_EMAIL = encode_for_database(columns[231]),
                                    REVISION_CODE_1 = encode_for_database(columns[232]),
                                    REVISION_CODE_2 = encode_for_database(columns[233]),
                                    METAL_INDICATOR = encode_for_database(columns[234])
                                ).save()
                            except:
                                print("toxic release")
                                print("couldn't add: ", columns)
                print("finished", unzipped_file_path)

        for year in range(1990, 2016):
            filename = "annual_all_"+str(year)+".zip"
            download_url = "http://aqsdr1.epa.gov/aqsweb/aqstmp/airdata/"+filename  
            tmp_path = temp_dir
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"annual_all_"+str(year)+".csv"

            print("working on ", unzipped_file_path)

            if os.path.isfile(unzipped_file_path):
                with open(unzipped_file_path, 'r') as f:
                    is_first_line = True
                    index_to_column = {}
                    counter = 0
                    for line in f:
                        counter = counter + 1
                        if counter % 1000 == 0:
                            print(counter)
                        columns = line.split(",")
                        if is_first_line:
                            for column_index, column in enumerate(columns):
                                index_to_column[column_index] = column
                                if not RawDataMap.objects.filter(import_id="air quality", identifier=column).exists():
                                    RawDataMap(import_id="air quality", identifier=column).save()
                            is_first_line = False
                        else:
                            try:
                                AirQualityDataPoint(
                                    State_Code = encode_for_database(columns[0]),
                                    County_Code = encode_for_database(columns[1]),
                                    Site_Num = encode_for_database(columns[2]),
                                    Parameter_Code = encode_for_database(columns[3]),
                                    POC = encode_for_database(columns[4]),
                                    Latitude = encode_for_database(columns[5]),
                                    Longitude = encode_for_database(columns[6]),
                                    Datum = encode_for_database(columns[7]),
                                    Parameter_Name = encode_for_database(columns[8]),
                                    Sample_Duration = encode_for_database(columns[9]),
                                    Pollutant_Standard = encode_for_database(columns[10]),
                                    Metric_Used = encode_for_database(columns[11]),
                                    Method_Name = encode_for_database(columns[12]),
                                    Year = encode_for_database(columns[13]),
                                    Units_of_Measure = encode_for_database(columns[14]),
                                    Event_Type = encode_for_database(columns[15]),
                                    Observation_Count = encode_for_database(columns[16]),
                                    Observation_Percent = encode_for_database(columns[17]),
                                    Completeness_Indicator = encode_for_database(columns[18]),
                                    Valid_Day_Count = encode_for_database(columns[19]),
                                    Required_Day_Count = encode_for_database(columns[20]),
                                    Exceptional_Data_Count = encode_for_database(columns[21]),
                                    Null_Data_Count = encode_for_database(columns[22]),
                                    Primary_Exceedance_Count = encode_for_database(columns[23]),
                                    Secondary_Exceedance_Count = encode_for_database(columns[24]),
                                    Certification_Indicator = encode_for_database(columns[25]),
                                    Num_Obs_Below_MDL = encode_for_database(columns[26]),
                                    Arithmetic_Mean = encode_for_database(columns[27]),
                                    Arithmetic_Standard_Dev = encode_for_database(columns[28]),
                                    onest_Max_Value = encode_for_database(columns[29]),
                                    onest_Max_DateTime = encode_for_database(columns[30]),
                                    twod_Max_Value = encode_for_database(columns[31]),
                                    twond_Max_DateTime = encode_for_database(columns[32]),
                                    threerd_Max_Value = encode_for_database(columns[33]),
                                    threerd_Max_DateTime = encode_for_database(columns[34]),
                                    fourthth_Max_Value = encode_for_database(columns[35]),
                                    fourthth_Max_DateTime = encode_for_database(columns[36]),
                                    onest_Max_Non_Overlapping_Value = encode_for_database(columns[37]),
                                    onest_NO_Max_DateTime = encode_for_database(columns[38]),
                                    twond_Max_Non_Overlapping_Value = encode_for_database(columns[39]),
                                    twond_NO_Max_DateTime = encode_for_database(columns[40]),
                                    ninenineth_Percentile = encode_for_database(columns[41]),
                                    nineeightth_Percentile = encode_for_database(columns[42]),
                                    ninefiveth_Percentile = encode_for_database(columns[43]),
                                    ninezeroth_Percentile = encode_for_database(columns[44]),
                                    sevenfiveth_Percentile = encode_for_database(columns[45]),
                                    fivezeroth_Percentile = encode_for_database(columns[46]),
                                    onezeroth_Percentile = encode_for_database(columns[47]),
                                    Local_Site_Name = encode_for_database(columns[48]),
                                    Address = encode_for_database(columns[49]),
                                    State_Name = encode_for_database(columns[50]),
                                    County_Name = encode_for_database(columns[51]),
                                    City_Name = encode_for_database(columns[52]),
                                    CBSA_Name = encode_for_database(columns[53]),
                                    Date_of_Last_Change = encode_for_database(columns[54])
                                ).save()
                            except:
                                print("couldn't add: ", columns)

