from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField(null=True, blank=True)  # Verifica este campo

    def __str__(self):  
        return self.nombre

