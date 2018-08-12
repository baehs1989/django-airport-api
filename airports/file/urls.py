from django.conf.urls import url
from . import views

app_name = "file"

urlpatterns = [
    url(r'^$', views.list, name="upload"),
    url(r'^success$', views.success, name="success"),
    url(r'^files$', views.FileList.as_view(), name="files"),
]