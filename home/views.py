from home.models import AirQualityDataPoint, ToxicDataPoint
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.routers import DefaultRouter

import django_filters


### AIR QUALITY DATA ###
class AirQualityDataPointSerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.CharField(source="Latitude", max_length=1000)
    longitude = serializers.CharField(source="Longitude", max_length=1000)

    class Meta:
        model = AirQualityDataPoint
        fields = ["latitude", "longitude", "id"]


class AirQualityDataPointFilter(django_filters.FilterSet):
    min_latitude = django_filters.NumberFilter(name="Latitude", lookup_type='gte')
    max_latitude = django_filters.NumberFilter(name="Latitude", lookup_type='lte')
    min_longitude = django_filters.NumberFilter(name="Longitude", lookup_type='gte')
    max_longitude = django_filters.NumberFilter(name="Longitude", lookup_type='lte')

    class Meta:
        model = AirQualityDataPoint
        filter_fields = ('Year','min_latitude', 'max_latitude','min_longitude', 'max_longitude')

class AirQualityDataPointViewSet(viewsets.ModelViewSet):
    queryset = AirQualityDataPoint.objects.all()
    serializer_class = AirQualityDataPointSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AirQualityDataPointFilter



### TOXIC DATA ###

class ToxicDataPointSerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.CharField(source="LATITUDE", max_length=1000)
    longitude = serializers.CharField(source="LONGITUDE", max_length=1000)

    class Meta:
        model = ToxicDataPoint
        fields = ["latitude", "longitude", "id"]

class ToxicDataPointFilter(django_filters.FilterSet):
    min_latitude = django_filters.NumberFilter(name="LATITUDE", lookup_type='gte')
    max_latitude = django_filters.NumberFilter(name="LATITUDE", lookup_type='lte')
    min_longitude = django_filters.NumberFilter(name="LONGITUDE", lookup_type='gte')
    max_longitude = django_filters.NumberFilter(name="LONGITUDE", lookup_type='lte')

    class Meta:
        model = ToxicDataPoint
        filter_fields = ('REPORTING_YEAR','min_latitude', 'max_latitude','min_longitude', 'max_longitude')


class ToxicDataPointViewSet(viewsets.ModelViewSet):
    queryset = ToxicDataPoint.objects.all()
    serializer_class = ToxicDataPointSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ToxicDataPointFilter



router = DefaultRouter()

router.register(r'airquality', AirQualityDataPointViewSet)
router.register(r'toxic', ToxicDataPointViewSet)