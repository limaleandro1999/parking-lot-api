"""parkinglot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from parkinglot.drivers.urls import urlpatterns as drivers_urls
from parkinglot.cars.urls import urlpatterns as cars_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Parking Lot API docs",
        default_version="v1",
        contact=openapi.Contact(email="limaleandro1999@gmail.com")
    ),
    public=True,
    permission_classes=(
        permissions.AllowAny,
    )
)

swagger_views = schema_view.with_ui('swagger', cache_timeout=0)

api_urls = [
    *drivers_urls,
    *cars_urls,
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('docs/', swagger_views, name="docs")
]
