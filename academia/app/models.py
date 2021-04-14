from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to='static/img')

    def __str__(self):         
        return str(self.nombre)


    
    
