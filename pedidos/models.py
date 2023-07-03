from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 100)
    email = models.EmailField(blank = True, null = True)
    telefono = models.CharField(max_length = 10)

class Productos(models.Model):
    nombre = models.CharField(max_length = 50)
    seccion = models.CharField(max_length = 50)
    precio = models.FloatField()

    def __str__(self) -> str:
        return 'El nombre es %s la sección es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()