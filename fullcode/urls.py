from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *
from verification.views import CertificateVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('advantages', AdvantageViewSet)
router.register('leads', LeadViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Fullcode API",
        default_version='v1'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path(
        'certificate/<str:certificate_id>/',
        CertificateVerifyView.as_view(),
        name='certificate-verify'
    ),

    path('swagger/', schema_view.with_ui('swagger')),
    path('i18n/', include('django.conf.urls.i18n')),
]
