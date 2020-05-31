from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.select_apps.views import list_heroes, get_heroes_id
from apps.select_related_apps.views import list_vehicles, get_vehicle_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_heroes/', list_heroes),
    url(r'^list_heroes/(?P<pk>[0-9]+)$', get_heroes_id),

    path('list_vehicles/', list_vehicles),
    url(r'^list_vehicles/(?P<pk>[0-9]+)$', get_vehicle_id)
]
