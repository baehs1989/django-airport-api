from django.conf.urls import url
from . import views

app_name = "airport"

urlpatterns = [
    url(r'^list', views.AirportList.as_view(), name="list"),
]