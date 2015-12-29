from home.models import AirQualityDataPoint, ToxicDataPoint
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework import status
import itertools
import django_filters
from math import radians, cos, sin, asin, sqrt
from django.shortcuts import render


def full_map(request):
    return render(request, 'map.html')

class MapScoreAPIView(APIView):

    default_grade = [1, "Good", "No Air Quality Data"]
    approx_degree_to_meter = 100000.0

    standards = {
        "Ozone 1-hour Daily 2005": {
        #Ozone unit is stored as ppm, but we need to convert to ppb
            "func": lambda x: float(x)*1000,
            "grades": [
                [[0, 124], 1, "Good"],
                [[125, 164], 3, "Unhealthy for Sensitive Groups"],
                [[164, 204], 4, "Unhealthy"],
                [[204, 404], 5, "Very Unhealthy"],
                [[404, 504], 6, "Hazardous"],
                [[504, 100000], 7, "Very Hazardous"],
            ]
        },
        "Ozone 8-Hour 1997": {
        #Ozone unit is stored as ppm, but we need to convert to ppb
            "func": lambda x: float(x)*1000,
            "grades": [
                [[0, 54], 1, "Good"],
                [[54, 70], 2, "Moderate"],
                [[70, 85], 3, "Unhealthy for Sensitive Groups"],
                [[85, 105], 4, "Unhealthy"],
                [[105, 100000], 5, "Very Unhealthy"],
            ]
        },
        "PM25 24-hour 2006": {
        #PM25 unit is micrograms / cubic meter - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 12], 1, "Good"],
                [[12.1, 35.4], 2, "Moderate"],
                [[35.5, 55.4], 3, "Unhealthy for Sensitive Groups"],
                [[55.5, 150.4], 4, "Unhealthy"],
                [[150.5, 250.4], 5, "Very Unhealthy"],
                [[250.5, 350.4], 6, "Hazardous"],
                [[350.5, 100000], 7, "Very Hazardous"],
            ]
        },
        "PM25 24-hour 2013": {
        #PM25 unit is micrograms / cubic meter - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 12], 1, "Good"],
                [[12.1, 35.4], 2, "Moderate"],
                [[35.5, 55.4], 3, "Unhealthy for Sensitive Groups"],
                [[55.5, 150.4], 4, "Unhealthy"],
                [[150.5, 250.4], 5, "Very Unhealthy"],
                [[250.5, 350.4], 6, "Hazardous"],
                [[350.5, 100000], 7, "Very Hazardous"],
            ]
        },
        "PM10 24-hour 2006": {
        #PM25 unit is micrograms / cubic meter - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 54], 1, "Good"],
                [[55, 154], 2, "Moderate"],
                [[155, 254], 3, "Unhealthy for Sensitive Groups"],
                [[255, 354], 4, "Unhealthy"],
                [[355, 424], 5, "Very Unhealthy"],
                [[425, 504], 6, "Hazardous"],
                [[505, 100000], 7, "Very Hazardous"],
            ]
        },
        "CO 8-hour 1971": {
        #CO unit is stored as parts per million - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 4.4], 1, "Good"],
                [[4.5, 9.4], 2, "Moderate"],
                [[9.5, 12.4], 3, "Unhealthy for Sensitive Groups"],
                [[12.5, 15.4], 4, "Unhealthy"],
                [[15.5, 30.4], 5, "Very Unhealthy"],
                [[30.5, 40.4], 6, "Hazardous"],
                [[40.5, 100000], 7, "Very Hazardous"],
            ]
        },
        "SO2 1-hour 2010": {
        # SO unit is parts per billion - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 35], 1, "Good"],
                [[46, 75], 2, "Moderate"],
                [[76, 185], 3, "Unhealthy for Sensitive Groups"],
                [[186, 304], 4, "Unhealthy"],
                [[305, 604], 5, "Very Unhealthy"],
                [[605, 804], 6, "Hazardous"],
                [[805, 100000], 7, "Very Hazardous"],
            ]
        },
        "SO2 24-hour 1971": {
        # SO unit is parts per billion - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 35], 1, "Good"],
                [[46, 75], 2, "Moderate"],
                [[76, 185], 3, "Unhealthy for Sensitive Groups"],
                [[186, 304], 4, "Unhealthy"],
                [[305, 604], 5, "Very Unhealthy"],
                [[605, 804], 6, "Hazardous"],
                [[805, 100000], 7, "Very Hazardous"],
            ]
        },
        "NO2 1-hour": {
        # NO unit is parts per billion - no conversion needed
            "func": lambda x: float(x),
            "grades": [
                [[0, 53], 1, "Good"],
                [[54, 100], 2, "Moderate"],
                [[101, 360], 3, "Unhealthy for Sensitive Groups"],
                [[361, 649], 4, "Unhealthy"],
                [[650, 1249], 5, "Very Unhealthy"],
                [[1250, 1649], 6, "Hazardous"],
                [[1650, 100000], 7, "Very Hazardous"],
            ]
        },
    }

    def get_standards(self):
        return self.standards

    def get_single_air_quality_score(self, point):
        grading_report  = self.get_standards()[point['Pollutant_Standard']]
        grades          = grading_report['grades']
        transmute_func  = grading_report['func']
        localized_score = transmute_func(point['Arithmetic_Mean'])

        found_grades = filter(lambda grade: grade[0][0] <= localized_score < grade[0][1], grades)

        if found_grades:
            return [found_grades[0][1], found_grades[0][2], point['Pollutant_Standard']]
        else: 
            return self.default_grade

    def haversine(self, lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        km = 6367 * c
        return km

    def get_list_of_points(self):
        if self.filter_type == 1: 
            return AirQualityDataPoint.objects.filter(
                Pollutant_Standard__in = self.standards.keys(),
                Latitude__gte = float(self.min_latitude),
                Latitude__lte = float(self.max_latitude),
                Longitude__gte = float(self.min_longitude),
                Longitude__lte = float(self.max_longitude),
                Year  = self.year
            ).values("Pollutant_Standard", "Arithmetic_Mean", "Latitude", "Longitude")        
        else:
            return filter(
                lambda p: self.haversine(self.latitude, self.longitude, p['Latitude'], p['Longitude']) < self.radius,
                AirQualityDataPoint.objects.filter(
                    Pollutant_Standard__in = self.standards.keys(),
                    Latitude__gt = float(self.latitude) - self.radius / self.approx_degree_to_meter,
                    Latitude__lte = float(self.latitude) + self.radius / self.approx_degree_to_meter,
                    Longitude__gt = float(self.longitude) - self.radius / self.approx_degree_to_meter,
                    Longitude__lt = float(self.longitude) + self.radius / self.approx_degree_to_meter,
                    Year  = self.year,
                    
                ).values("Pollutant_Standard", "Arithmetic_Mean", "Latitude", "Longitude")
            )

    def get_total_air_quality_score(self):
        intersecting_quality_points = self.get_list_of_points()

        scores = [self.get_single_air_quality_score(point) for point in intersecting_quality_points]
        packaged_score = {
            "max_grade": max(scores) if scores else self.default_grade,
            "results": [self.get_single_air_quality_score(point) for point in intersecting_quality_points]
        }
        return packaged_score

    def get(self, request, *args, **kw):
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [],
        }
        response = Response(result, status=status.HTTP_200_OK)

        # to do add error checking. 

        self.filter_type = int(request.GET.get("filter_type", 2))
        if self.filter_type == 1:
            self.min_latitude   = request.GET.get("min_latitude", 38.84024244214068)
            self.max_latitude   = request.GET.get("max_latitude", 38.940585268033)
            self.min_longitude  = request.GET.get("min_longitude", -77.11629867553711)
            self.max_longitude  = request.GET.get("max_longitude", -76.86910629272461)
        else:
            self.latitude       = float(request.GET.get("latitude", 38.84024244214068))
            self.longitude      = float(request.GET.get("longitude", -76.86910629272461))
            self.radius         = float(request.GET.get("radius", 3218.69))
        self.year       = request.GET.get("year", 2012)

        score = self.get_total_air_quality_score()

        result["results"].append({
            "latitude": self.latitude,
            "longitude": self.longitude,
            "title": "Air Quality Score: " + score['max_grade'][1],
            "grade": (8.0 - float(score['max_grade'][0])) / 7.0 * 100.0,
            "results": score['results'],
            "universe": "quality",
        })
        return response



### AIR QUALITY DATA ###
class AirQualityDataPointSerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.CharField(source="Latitude", max_length=1000)
    longitude = serializers.CharField(source="Longitude", max_length=1000)
    title = serializers.SerializerMethodField()
    year = serializers.CharField(source="Year", max_length=1000)
    universe = serializers.SerializerMethodField()

    def get_universe(self, obj):
        return "air"

    def get_title(self, obj):
        return str(obj)

    class Meta:
        model = AirQualityDataPoint
        fields = ["latitude", "longitude", "id", "title", "year", "universe"]


class AirQualityDataPointFilter(django_filters.FilterSet):
    min_latitude = django_filters.NumberFilter(name="Latitude", lookup_type='gte')
    max_latitude = django_filters.NumberFilter(name="Latitude", lookup_type='lte')
    min_longitude = django_filters.NumberFilter(name="Longitude", lookup_type='gte')
    max_longitude = django_filters.NumberFilter(name="Longitude", lookup_type='lte')
    year = django_filters.NumberFilter(name="Year")

    class Meta:
        model = AirQualityDataPoint
        filter_fields = ('year','min_latitude', 'max_latitude','min_longitude', 'max_longitude')

class AirQualityDataPointViewSet(viewsets.ModelViewSet):
    queryset = AirQualityDataPoint.objects.all()
    serializer_class = AirQualityDataPointSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AirQualityDataPointFilter

    def get_queryset(self):
        m = MapScoreAPIView()
        queryset = super(AirQualityDataPointViewSet, self).get_queryset().filter(Pollutant_Standard__in = m.standards.keys())
        return queryset




### TOXIC DATA ###

class ToxicDataPointSerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.CharField(source="LATITUDE", max_length=1000)
    longitude = serializers.CharField(source="LONGITUDE", max_length=1000)
    title = serializers.SerializerMethodField()
    year = serializers.CharField(source="REPORTING_YEAR", max_length=1000)
    universe = serializers.SerializerMethodField()

    def get_universe(self, obj):
        return "toxic"

    def get_title(self, obj):
        return str(obj)

    class Meta:
        model = ToxicDataPoint
        fields = ["latitude", "longitude", "id", "title", "year", "universe"]

class ToxicDataPointFilter(django_filters.FilterSet):
    min_latitude = django_filters.NumberFilter(name="LATITUDE", lookup_type='gte')
    max_latitude = django_filters.NumberFilter(name="LATITUDE", lookup_type='lte')
    min_longitude = django_filters.NumberFilter(name="LONGITUDE", lookup_type='gte')
    max_longitude = django_filters.NumberFilter(name="LONGITUDE", lookup_type='lte')
    year = django_filters.NumberFilter(name="REPORTING_YEAR")

    class Meta:
        model = ToxicDataPoint
        filter_fields = ('year','min_latitude', 'max_latitude','min_longitude', 'max_longitude')


class ToxicDataPointViewSet(viewsets.ModelViewSet):
    queryset = ToxicDataPoint.objects.all()
    serializer_class = ToxicDataPointSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ToxicDataPointFilter

#scoring API




router = DefaultRouter()

router.register(r'airquality', AirQualityDataPointViewSet)
router.register(r'toxic', ToxicDataPointViewSet)