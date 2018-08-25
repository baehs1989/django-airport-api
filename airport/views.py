from django.shortcuts import render
from django.views import generic
from . import models

#API
from rest_framework import viewsets
from . import serializers
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import filters
from rest_framework import pagination

# Create your views here.
class AirportList(generic.ListView):
    model = models.Airport
    paginate_by = 15
    template_name = 'airports/airport_list.html'
    context_object_name = 'airport_list'


class StandardResultsSetPagination(pagination.PageNumberPagination):
    # custom pagination setup
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100000

class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AirportSerializer
    queryset = models.Airport.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AirportApiPermission, permissions.IsSuperUser)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('country', 'name', 'iata', 'city')
    pagination_class = StandardResultsSetPagination