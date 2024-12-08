from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreditoForm, Credito
from django.utils.timezone import now


# Create your views here.
def agregar_credito(request):
    data = {
        'form': CreditoForm()
    }

    if request.method == 'POST':
        formulario = CreditoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado Correctamente'
            return redirect('creditos:listar_credito')  # Redirigir después de guardar
        else:
            data['form'] = formulario
            data['mensaje'] = 'Por favor, corrige los errores'

    return render(request, 'creditos/agregar_credito.html', data)



def listar_credito(request):
    creditos = Credito.objects.all()
    hoy = now().date()

    for credito in creditos:
        credito.dias_restantes = (credito.fecha_vencimiento - hoy).days

    return render(request, 'creditos/listar_credito.html', {'creditos': creditos})



def modificar_credito(request, id):

    credito = get_object_or_404(Credito, id=id)

    data = {
        'form': CreditoForm(instance=credito)
    }

    if request.method == 'POST':
        formulario = CreditoForm(data= request.POST, instance=credito) 
        if formulario.is_valid():
            formulario.save()
            return redirect('creditos:listar_credito')
        data['form'] = formulario
        
    

    return render(request, 'creditos/modificar_credito.html', data)


def eliminar_credito(request, id):
    credito = get_object_or_404(Credito, id=id)
    credito.delete()
    return redirect('creditos:listar_credito')