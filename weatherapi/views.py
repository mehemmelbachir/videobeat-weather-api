from django.shortcuts import render, redirect
from .models import InputData, OutputData
from . import services

# Create your views here.
def home(request):
    template_name = 'weatherapi\index.html'
    services.calculate_output_data()
    return render(request, template_name)


def clear_data(request):
    InputData.objects.all().delete()
    OutputData.objects.all().delete()
    return redirect('/')

