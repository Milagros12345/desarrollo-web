from django.db import models

# Create your models here.
#creamos nuestras tablas
class clientes(models.Model):
    #creamos campos de nuestra tabla
    nombre=models.CharField(max_length=30)#tipo
    direccion=models.CharField(max_length=50, verbose_name="La dirección")
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'el nombre es %s la seccion es %s y el precio es %s '%(self.nombre,self.seccion,self.precio)

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

