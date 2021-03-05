from django.shortcuts import render
from django.views import generic
from .models import Car

class CarsIndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all()

