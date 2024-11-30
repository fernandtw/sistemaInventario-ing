from django.db import models

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=45)
    apellido_cliente = models.CharField(max_length=45)
    telefono_cliente = models.CharField(max_length=15)

   
    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"
