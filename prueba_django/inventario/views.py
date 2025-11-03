from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Producto
from .forms import ProductoForm

# Create your views here.
# DRF imports for API view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductoSerializer

@login_required
def index(request):
    productos = Producto.objects.all().order_by('-id')
    paginator = Paginator(productos, 6)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'inventario/index.html', {'page_obj': page_obj})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?creado=1')
    else:
        form = ProductoForm()

    return render(request, 'inventario/product_form.html', {'form': form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/?actualizado=1')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'inventario/product_form.html', {'form': form, 'editar': True})

@login_required
def eliminar_producto(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return redirect('/?eliminado=1')

# API
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_productos(request):
    productos = Producto.objects.order_by("-fecha_creacion")
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)
