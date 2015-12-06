from django.core.management.base import BaseCommand, CommandError
from django.db import connection
import os.path
import zipfile
import urllib
from home.models import RawDataMap, DataPoint

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("import raw data")

        connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")
        DataPoint.objects.all().delete()

        for year in range(1987, 2014):
            filename = "US_"+str(year)+"_v13.zip"
            download_url = "http://www3.epa.gov/tri/"+filename
            tmp_path = "./tmp/"
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"US_1_"+str(year)+"_v13.txt"

            if not os.path.isfile(file_path):
                urllib.urlretrieve(download_url, file_path)
                print("downloaded: "+file_path)

            if os.path.isfile(file_path):
                with zipfile.ZipFile(file_path, "r") as z:
                    z.extractall(tmp_path)


            if os.path.isfile(unzipped_file_path):
                with open(unzipped_file_path, 'r') as f:
                    is_first_line = True
                    index_to_column = {}
                    for line in f:
                        columns = line.split("\t")
                        if is_first_line:
                            for column_index, column in enumerate(columns):
                                index_to_column[column_index] = column
                                if not RawDataMap.objects.filter(import_id="toxic release", identifier=column).exists():
                                    RawDataMap(import_id="toxic release", identifier=column).save()
                            is_first_line = False
                        else:
                            for column_index, column in enumerate(columns):
                                DataPoint(
                                    data_set="toxic release",
                                    column_value=index_to_column[column_index],
                                    point_value=str(column)
                                ).save()

        for year in range(1990, 2016):
            filename = "annual_all_"+str(year)+".zip"
            download_url = "http://aqsdr1.epa.gov/aqsweb/aqstmp/airdata/"+filename  
            tmp_path = "./tmp/"
            file_path = tmp_path+filename
            unzipped_file_path = tmp_path+"annual_all_"+str(year)+".csv"

            if not os.path.isfile(file_path):
                urllib.urlretrieve(download_url, file_path)
                print("downloaded: "+file_path)

            if os.path.isfile(file_path):
                with zipfile.ZipFile(file_path, "r") as z:
                    z.extractall(tmp_path)

            if os.path.isfile(unzipped_file_path):
                with open(unzipped_file_path, 'r') as f:
                    is_first_line = True
                    index_to_column = {}
                    for line in f:
                        columns = line.split(",")
                        if is_first_line:
                            for column_index, column in enumerate(columns):
                                index_to_column[column_index] = column
                                if not RawDataMap.objects.filter(import_id="air quality", identifier=column).exists():
                                    RawDataMap(import_id="air quality", identifier=column).save()
                            is_first_line = False
                        else:
                            for column_index, column in enumerate(columns):
                                DataPoint(
                                    data_set="air quality",
                                    column_value=index_to_column[column_index],
                                    point_value=str(column)
                                ).save()

