from django.shortcuts import render
from blog.models import ofertas
# Create your views here.

def blog(request):
    ofertas_i= ofertas.objects.all()
    return render(request, 'blog/blog.html', {'ofertas_i':ofertas_i})