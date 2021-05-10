from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to='static/img')
    texto  = models.TextField(max_length=20000, null=True)
    video1 = models.TextField(max_length=20000,null=True,blank=True)
    video2 = models.TextField(max_length=20000,null=True,blank=True)
    video3 = models.TextField(max_length=20000,null=True,blank=True)
    video4 = models.TextField(max_length=20000,null=True,blank=True)
    forex = models.BooleanField(default=False)
    cripto = models.BooleanField(default=False)
    otro = models.BooleanField(default=False)




    

    def __str__(self):         
        return str(self.nombre)



    


