from django import forms
from .models import Credito


class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = '__all__'
        
    fecha = forms.DateField(
        label="Fecha De Otorgacion de credito",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    fecha_vencimiento = forms.DateField(
        label="Fecha De Vencimiento",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
        

      
