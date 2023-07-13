import requests
from django.core.files.base import ContentFile
from asyncio.windows_events import NULL
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.core.files.base import ContentFile
from .models import Producto_Api

# Create your views here.

def product_list(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'crud/product-list.html', context)
    else:
        return render(request, '404.html')

def product_new(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto.objects.create(
                idProducto = idProducto,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen,
                marca = marca
            )
            obj.save()
            return redirect(reverse('product-list') + "?OK")
        else:
            return redirect(reverse('product-list') + "?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/product-new.html',{'form':form})

def product_detail(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product-detail.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")
        
def product_edit(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            form = ProductoForm(instance = producto)
        else:
            return redirect(reverse('product-list') + "?FAIL")
    
        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('product-list') + "?OK")
            else:
                return redirect(reverse('product-update') + product_id)
        return render(request,'crud/product-update.html',{'form':form})   
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(to = 'product-list')
    except:
        return redirect(reverse('product-list') + "?FAIL")
    
#Funcion para integrar la API a la BDD
def integrarAPIaBDD(request):
    #Aqui llamamos a la api del profesor
    response = requests.get('https://musicpro.bemtorres.win/api/v1/bodega/producto')
    data = response.json()

    #aqui recorreremos los productos del json, los igualaremos al los datos
    #que tenemos en el modelo y ademas aprovecharemos de descargar la imagen
    for producto_api_data in data:
            idProductoApi = producto_api_data['id']
            codigo = producto_api_data['codigo']
            nombre = producto_api_data['nombre']
            descripcion = producto_api_data['descripcion']
            precio = producto_api_data['precio']
            precio_raw = producto_api_data['precio_raw']
            asset = producto_api_data['asset']
            asset_raw = producto_api_data['asset_raw']
            estado = producto_api_data['estado']

            # Descargar y guardar la imagen en el modelo
            image_content = requests.get(asset).content
            producto_api = Producto_Api(
                idProductoApi=idProductoApi,
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
                producto_imagen=ContentFile(image_content),
                precio=precio,
                precio_raw=precio_raw,
                asset=asset,
                asset_raw=asset_raw,
                estado=estado
            )
            producto_api.save()
