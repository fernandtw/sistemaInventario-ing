from django.db import models
from clientesCrudApp.models import Cliente
from productos.models import Producto

# Create your models here.
class Credito(models.Model):
    class DeudaChoices(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        PAGADA = 'Pagada', 'Pagada'
        CANCELADA = 'Cancelada', 'Cancelada'
        
    class PagoChoices(models.TextChoices):
        NoPago = 'No pagado', 'No pagado'
        Efectivo = 'Efectivo', 'Efectivo'
        Tarjeta = 'Tarjeta', 'Tarjeta'
        Transferencia = 'Transferencia', 'Transferencia'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    deuda = models.CharField(
        max_length=10,
        choices=DeudaChoices.choices,
        default=DeudaChoices.PENDIENTE,
    )
    fecha = models.DateField()
    fecha_vencimiento = models.DateField(null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=50,
        choices=PagoChoices.choices,
        default=PagoChoices.NoPago,
    )

    def __str__(self):
        return f"{self.cliente} - {self.monto} - {self.deuda}"

        