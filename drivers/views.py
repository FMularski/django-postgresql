from django.shortcuts import render
from django.views import  generic
from .models import Driver
from .forms import DriverForm
from django.http import HttpResponse

class DriversIndexView(generic.ListView):
    template_name = 'drivers/index.html'
    context_object_name = 'drivers'

    def get_queryset(self):
        return Driver.objects.all()


class DriversDetailView(generic.DetailView):
    template_name = 'drivers/detail.html'
    model = Driver


def create(request):
    if request.method == 'GET':
        form = DriverForm()
    else:
        form = DriverForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')
            
    return render(request, 'drivers/create.html', {'form': form})