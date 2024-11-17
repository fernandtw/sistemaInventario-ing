from django import forms
from django.contrib.auth.models import User
from .models import Perfil

from django.core.exceptions import ValidationError
import re

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']

    def clean_password_confirmacion(self):
        password = self.cleaned_data.get('password')
        password_confirmacion = self.cleaned_data.get('password_confirmacion')

        # Verificar que las contraseñas coincidan
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        # Validaciones adicionales
        self.validate_password_strength(password)

        return password_confirmacion

    def validate_password_strength(self, password):
        """
        Validar la fortaleza de la contraseña según varias reglas.
        """
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if not any(char.isdigit() for char in password):
            raise ValidationError("La contraseña debe contener al menos un número.")

        if not any(char.isalpha() for char in password):
            raise ValidationError("La contraseña debe contener al menos una letra.")

        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/`~' for char in password):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")

        if password.lower() in ['password', '123456', '12345678', 'qwerty', 'abc123']:
            raise ValidationError("No utilices contraseñas comunes o fácilmente adivinables.")
