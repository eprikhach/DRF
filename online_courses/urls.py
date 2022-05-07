from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import UserActivationView

schema_view = get_schema_view(
    openapi.Info(
        title="Recourse API",
        default_version='v1',
        description="Development API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rikhen@icloud.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=tuple([AllowAny]),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/', include('api.urls')),
]
