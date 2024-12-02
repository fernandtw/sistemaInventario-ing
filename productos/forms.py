from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(
        label="Fecha Vencimiento",
        required=False,  # Cambia a False si el campo es opcional
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'fecha_vencimiento']
 

