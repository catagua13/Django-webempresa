from django.shortcuts import render
from services.models import servicios

# Create your views here.
def services(request):
    servicios_i= servicios.objects.all()
    return render(request, 'services/services.html', {'servicios_i':servicios_i})