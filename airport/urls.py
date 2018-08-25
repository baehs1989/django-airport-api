from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter

app_name = "airport"

router = DefaultRouter()
router.register('airport', views.AirportViewSet)

urlpatterns = [
    url(r'^list', views.AirportList.as_view(), name="list"),
    url(r'api/', include(router.urls),)
]