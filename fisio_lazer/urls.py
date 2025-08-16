from django.urls import path
from . import views

urlpatterns = [
 path("fisio_lazer/", views.home, name="home" )   
]
