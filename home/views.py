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

class MapScoreAPIView(APIView):

    default_grade = [1, "Good"]

    standards = {
        "Ozone 1-hour Daily 2005": {
            "func": lambda x: float(x)*1000,
            "grades": [
                [[125, 164], 3, "Unhealthy for Sensitive Groups"],
                [[164, 204], 4, "Unhealthy"],
                [[204, 404], 5, "Very Unhealthy"],
                [[404, 504], 6, "Hazardous"],
                [[504, 100000], 7, "Very Hazardous"],
            ]
        },
        "Ozone 8-Hour 1997": {
            "func": lambda x: float(x)*1000,
            "grades": [
                [[0, 54], 1, "Good"],
                [[54, 70], 2, "Moderate"],
                [[70, 85], 3, "Unhealthy for Sensitive Groups"],
                [[85, 105], 4, "Unhealthy"],
                [[105, 100000], 5, "Very Unhealthy"],
            ]
        },
        # "Ozone 8-Hour 2008": {
        # },
        # "PM25 24-hour 2006": {
        # },
        # "PM25 24-hour 2013": {
        # },
        # "PM10 24-hour 2006": {
        # },
        # "CO 8-hour 1971": {
        # },
        # "SO2 1-hour 2010": {
        # }
        # "SO2 24-hour 1971": {
        # },
        # "NO2 1-hour": {
        # },
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
            return found_grades[0][1], found_grades[0][2]
        else: 
            return self.default_grade

    def get_list_of_points(self):
        return AirQualityDataPoint.objects.filter(
            Pollutant_Standard__in = self.standards.keys(),
            Latitude__gte = float(self.min_latitude),
            Latitude__lte = float(self.max_latitude),
            Longitude__gte = float(self.min_longitude),
            Longitude__lte = float(self.max_longitude),
            Year  = self.year
        ).values("Pollutant_Standard", "Arithmetic_Mean", "Latitude", "Longitude")        

    def get_total_air_quality_score(self):
        intersecting_quality_points = self.get_list_of_points()
        scores = [self.get_single_air_quality_score(point) for point in intersecting_quality_points]
        return max(scores) 

    def get(self, request, *args, **kw):
        result = {}
        response = Response(result, status=status.HTTP_200_OK)
        self.min_latitude   = request.GET.get("min_latitude", 38.84024244214068)
        self.max_latitude   = request.GET.get("max_latitude", 38.940585268033)
        self.min_longitude  = request.GET.get("min_longitude", -77.11629867553711)
        self.max_longitude  = request.GET.get("max_longitude", -76.86910629272461)
        self.year       = request.GET.get("year", 2012)
        self.radius     = request.GET.get("radius")
        result['score'] = self.get_total_air_quality_score()
        return response



router = DefaultRouter()

router.register(r'airquality', AirQualityDataPointViewSet)
router.register(r'toxic', ToxicDataPointViewSet)