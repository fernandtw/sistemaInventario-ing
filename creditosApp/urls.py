from django.urls import path
from . import views


app_name = "creditos"

urlpatterns = [
  path('agregar-creditos/', views.agregar_credito, name='agregar_credito'),
  path('listar-creditos/', views.listar_credito, name='listar_credito'),
  path('modificar-creditos/<id>/', views.modificar_credito, name='modificar_credito'),
  path('eliminar-creditos/<id>/', views.eliminar_credito, name='eliminar_credito'),
]