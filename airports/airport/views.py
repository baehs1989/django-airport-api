from django.shortcuts import render
from django.views import generic
from .models import Airport


# Create your views here.
class AirportList(generic.ListView):
    model = Airport
    paginate_by = 15
    template_name = 'airports/airport_list.html'
    context_object_name = 'airport_list'