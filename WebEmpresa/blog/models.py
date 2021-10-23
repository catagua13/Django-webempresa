from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class categroias(models.Model):
    nombre= models.CharField(max_length=100)
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_modificacion= models.DateTimeField(auto_now=True)
    class Meta:
        db_table='categorias'
        verbose_name_plural='categorias'
        ordering = ['fecha_creacion']
    def __str__(self):
        return self.nombre

class ofertas(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_publicacion=models.DateTimeField(default=now)
    imagen=models.ImageField(upload_to='ofertas')
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    categorias= models.ManyToManyField(categroias)
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_modificacion= models.DateTimeField(auto_now=True)
    class Meta:
        db_table='ofertas'
        verbose_name_plural= 'ofertas'
    def __str__(self):
        return self.titulo
