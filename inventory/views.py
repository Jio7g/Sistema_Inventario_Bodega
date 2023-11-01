from django.shortcuts import render, redirect
from .models import Producto, RegistroSalida
from .forms import ProductoForm, RegistroSalidaForm

def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_inventario')
    else:
        form = ProductoForm()
    return render(request, 'ingresar_producto.html', {'form': form})

def registrar_salida(request):
    if request.method == 'POST':
        form = RegistroSalidaForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            cantidad = form.cleaned_data['cantidad']
            producto = Producto.objects.get(codigo=codigo)
            if producto.cantidad_existente >= cantidad:
                producto.cantidad_existente -= cantidad
                producto.save()
                RegistroSalida.objects.create(producto=producto, cantidad=cantidad)
                return redirect('consultar_inventario')
    else:
        form = RegistroSalidaForm()
    return render(request, 'registrar_salida.html', {'form': form})

def consultar_inventario(request):
    productos = Producto.objects.all()
    return render(request, 'consultar_inventario.html', {'productos': productos})
