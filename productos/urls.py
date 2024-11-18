from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),  # Ruta para agregar un producto
    path('productoseditar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),  # Ruta para eliminar un producto
    path('', views.listar_productos, name='listar_productos'),
]
