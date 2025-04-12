# mygis/urls.py

from django.contrib import admin
from django.urls import path
from gis_app import views  # import views از برنامه GIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.map_view, name='map'),  # مسیر جدید برای نقشه
]