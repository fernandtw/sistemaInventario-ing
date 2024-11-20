from django.urls import path
from clientesCrudApp import views

urlpatterns = [
    # ------------CRUD USUARIOS--------------------
    path("", views.listarCliente, name="listar_clientes"),
    path("clientes/agregar/", views.agregarCliente, name="agregar_cliente"),
    path("clientes/editar/<int:pk>/", views.editarCliente, name="editar_cliente"),
    path("clientes/eliminar/<int:pk>/", views.eliminarCliente, name="eliminar_cliente"),
]