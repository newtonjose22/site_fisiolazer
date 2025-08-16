
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fisio_lazer/", include("fisio_lazer.urls"))
]
