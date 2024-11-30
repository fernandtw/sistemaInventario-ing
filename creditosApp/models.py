from django.db import models

# Create your models here.
class Credito(models.Model):
    class DeudaChoices(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        PAGADA = 'Pagada', 'Pagada'
        CANCELADA = 'Cancelada', 'Cancelada'

    nombre = models.CharField(max_length=100)
    deuda = models.CharField(
        max_length=10,  # Longitud suficiente para las opciones de texto
        choices=DeudaChoices.choices,
        default=DeudaChoices.PENDIENTE,  # Valor por defecto opcional
    )
    fecha = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.deuda}"
        