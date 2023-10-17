

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("alunas/", include("alunas.urls")),
    path("admin/", admin.site.urls),
]