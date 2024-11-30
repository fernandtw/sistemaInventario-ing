from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm


def listarCliente(request):
    clientes = Cliente.objects.all() 
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

# Vista para agregar cliente
def agregarCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/AddClient.html', {'form': form})

# Vista para editar cliente
def editarCliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    # lógica para manejar el formulario de edición
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        # Crea el formulario con los datos enviados por el usuario
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()  # Guarda los cambios en el objeto existente
            return redirect('listar_clientes')  # Redirecciona a la lista de cliente
    else:
        # Crea el formulario con los datos actuales del cliente
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/EditClient.html', {'form': form, 'cliente': cliente})
    

   
# Vista para eliminar cliente
def eliminarCliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/clientes.html', {'cliente': cliente})
