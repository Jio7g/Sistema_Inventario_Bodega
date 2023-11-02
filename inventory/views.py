from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, RegistroSalida
from .forms import ProductoForm, RegistroSalidaForm
from django.core.paginator import Paginator
from django.db.models import Q

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

            try:
                # Intenta encontrar un producto con el código de barras escaneado.
                producto = Producto.objects.get(codigo_de_barras=codigo)
            except Producto.DoesNotExist:
                # Si el producto no se encuentra, muestra un mensaje de error.
                error_message = 'Producto no encontrado. Escanea otro código de barras.'
                return render(request, 'registrar_salida.html', {'form': form, 'error_message': error_message})

            if producto.cantidad_existente >= cantidad:
                # Si hay suficiente cantidad en el inventario, procesa la salida.
                producto.cantidad_existente -= cantidad
                producto.save()
                RegistroSalida.objects.create(producto=producto, cantidad=cantidad)
                return redirect('consultar_inventario')
            else:
                # Si la cantidad escaneada es mayor que la cantidad en inventario, muestra un mensaje de error.
                error_message = 'Cantidad insuficiente en el inventario.'
                return render(request, 'registrar_salida.html', {'form': form, 'error_message': error_message})

    else:
        form = RegistroSalidaForm()

    return render(request, 'registrar_salida.html', {'form': form})

def consultar_inventario(request):
    productos = Producto.objects.all()
    query = request.GET.get('q')  # Obtén el término de búsqueda del parámetro GET 'q'

    if query:
        # Utiliza Q para realizar una consulta OR entre nombre y código
        productos = productos.filter(Q(nombre__icontains=query) | Q(codigo__icontains=query))

    paginator = Paginator(productos, 5)  # Divide la lista de productos en páginas con 5 productos por página
    page = request.GET.get('page')
    productos = paginator.get_page(page)

    return render(request, 'consultar_inventario.html', {'productos': productos, 'query': query})