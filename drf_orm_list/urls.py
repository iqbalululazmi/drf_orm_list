from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.select_apps.views import list_heroes, get_heroes_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_heroes/', list_heroes),
    url(r'^list_heroes/(?P<pk>[0-9]+)$', get_heroes_id),
]
