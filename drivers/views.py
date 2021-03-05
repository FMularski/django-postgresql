from django.shortcuts import render
from django.views import  generic
from .models import Driver


class DriversIndexView(generic.ListView):
    template_name = 'drivers/index.html'
    context_object_name = 'drivers'

    def get_queryset(self):
        return Driver.objects.all()


class DriversDetailView(generic.DetailView):
    template_name = 'drivers/detail.html'
    model = Driver