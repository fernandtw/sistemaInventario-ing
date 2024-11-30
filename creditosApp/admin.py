from django.contrib import admin
from .models import Credito

# Register your models here.
@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'deuda', 'fecha', 'monto')  # Asegúrate de que los campos correctos estén aquí
    list_filter = ('fecha',)  # O puedes agregar otros filtros si es necesario
    search_fields = ('nombre',)