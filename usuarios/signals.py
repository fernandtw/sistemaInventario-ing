from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

# Función para crear o verificar un perfil de usuario al crear o actualizar un usuario
@receiver(post_save, sender=User)
def crear_o_verificar_perfil_usuario(sender, instance, created, **kwargs):
    if created:  # Si el usuario se acaba de crear
        Perfil.objects.create(user=instance)
    else:  # Si el usuario ya existía
        if not hasattr(instance, 'perfil'):  # Verificamos si tiene un perfil
            Perfil.objects.create(user=instance)  # Creamos el perfil si no existe

# Función para guardar el perfil de usuario al guardar un usuario
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'perfil'):  # Guardamos el perfil solo si existe
        instance.perfil.save()
