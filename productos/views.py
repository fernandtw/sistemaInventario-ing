from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from datetime import date, timedelta
from django.utils import timezone

# Vista para listar productos

def listar_productos(request):
    productos = Producto.objects.all()
    now = timezone.now().date()
    
    for producto in productos:
        # Cálculo correcto de vencido y próximo a vencer
        producto.vencido = now > producto.fecha_vencimiento
        producto.proximo_vencer = not producto.vencido and (producto.fecha_vencimiento - now).days <= 7
        
    return render(request, 'productos/listar.html', {
        'productos': productos
    })


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

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        # Obtener los datos del formulario manualmente
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        cantidad = request.POST.get('cantidad')
               

        # Reemplazar la coma por un punto en el precio, si es necesario
        if precio:
            precio = precio.replace(',', '.')

        # Actualizar el producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio  # Ya como un número decimal
        producto.fecha_vencimiento = fecha_vencimiento
        producto.cantidad = cantidad

        producto.save()  # Guarda los cambios

        return redirect('listar_productos')  # Redirige a la lista de productos
    else:
        # No es necesario hacer nada en el caso del GET, ya que los valores se pasarán al formulario
        pass

    return render(request, 'productos/editar.html', {'producto': producto})


    

   
# Vista para eliminar producto
def eliminar_producto(request, pk):
    # Obtenemos el producto con la primary key (pk) proporcionada
    producto = get_object_or_404(Producto, pk=pk)

    # Eliminamos el producto directamente
    producto.delete()

    # Redirigimos a la lista de productos
    return redirect('listar_productos')

