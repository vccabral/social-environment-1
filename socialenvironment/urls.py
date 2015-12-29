from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from home.models import RawDataMap, DataPoint, ToxicDataPoint, AirQualityDataPoint
from home.views import router, MapScoreAPIView, full_map

admin.site.register(RawDataMap)
admin.site.register(DataPoint)
admin.site.register(ToxicDataPoint)
admin.site.register(AirQualityDataPoint)

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', 'search.views.search', name='search'),

    url(r'^map/$', 'home.views.full_map', name='map'),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/map_score/$', MapScoreAPIView.as_view(), name='map_score'),
    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
