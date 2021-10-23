from django.db import models

# Create your models here.

class servicios(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=100)
    decripcion = models.TextField()
    imagen= models.ImageField(upload_to='servicios')
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='servicio'
        verbose_name='servicio'
    def __str__(self):
        return self.titulo
