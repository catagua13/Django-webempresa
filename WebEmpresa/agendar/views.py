from django.shortcuts import render
from agendar.models import agendar
# Create your views here.

def blog(request):
    agendar_i= agendar.objects.all()
    return render(request, 'blog/blog.html', {'agendar_i':agendar_i})