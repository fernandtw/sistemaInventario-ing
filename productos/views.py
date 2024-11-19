from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Vista para listar productos
# views.py

def listar_productos(request):
    productos = Producto.objects.all()  # Cambia Producto por el nombre de tu modelo si es diferente
    return render(request, 'productos/listar.html', {'productos': productos})

# Vista para agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar.html', {'form': form})

# Vista para editar producto
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    # lógica para manejar el formulario de edición
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        # Crea el formulario con los datos enviados por el usuario
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  # Guarda los cambios en el objeto existente
            return redirect('listar_productos')  # Redirecciona a la lista de productos
    else:
        # Crea el formulario con los datos actuales del producto
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar.html', {'form': form, 'producto': producto})
    

   
# Vista para eliminar producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/eliminar.html', {'producto': producto})

