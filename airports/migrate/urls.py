from django.conf.urls import url
from . import views

app_name = "migrate"

urlpatterns = [
    url(r'^$', views.list, name="migrate"),
    url(r'^migrations$', views.migrations, name="migrations"),
    url(r'^complete$', views.complete, name="complete"),
]