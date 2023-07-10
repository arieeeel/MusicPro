import requests
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from crud.models import *
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['POST'])
def transporte(request):
    url = 'http://music-pro.test/api/v1/transporte/seguimiento/68733MUSICPRO889365'

    response = requests.post(url)

    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        error_message = 'Ocurrió un error al enviar la solicitud POST'
        return Response({'detail': error_message}, status=response.status_code)



@api_view(['GET'])
@swagger_auto_schema(
    operation_description='Obtiene los productos de bodega',
    responses={
        200: 'Success',
        500: 'Internal Server Error',
    },
)
def getbodega(request):
    """
    obtener productos de bodega API.
    """
    url = "https://musicpro.bemtorres.win/api/v1/bodega/producto"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Aquí puedes trabajar con la respuesta del servidor
            return Response(data)  # Devolver una respuesta JSON con DRF
        else:
            error_message = "Error en la solicitud: " + str(response.status_code)
            return Response({"error": error_message}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)



@api_view(['GET'])
@swagger_auto_schema(
    operation_description='Obtener saludo',
    responses={
        200: 'Success',
        500: 'Internal Server Error',
    },
)
def saludo(request):
    """
    obtiene saludo de API.
    """
    url = "https://musicpro.bemtorres.win/api/v1/test/saludo"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Aquí puedes trabajar con la respuesta del servidor
            return Response(data)  # Devolver una respuesta JSON con DRF
        else:
            error_message = "Error en la solicitud: " + str(response.status_code)
            return Response({"error": error_message}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)



@api_view(['GET'])
@swagger_auto_schema(
    operation_description='obtener saldo',
    responses={
        200: 'Success',
        500: 'Internal Server Error',
    },
)
def saldo(request):
    """
    obtener saldo de API.
    """
    url = "https://musicpro.bemtorres.win/api/v1/test/saldo"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Aquí puedes trabajar con la respuesta del servidor
            return Response(data)  # Devolver una respuesta JSON con DRF
        else:
            error_message = "Error en la solicitud: " + str(response.status_code)
            return Response({"error": error_message}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)



@api_view(['GET', 'POST', 'DELETE'])
@swagger_auto_schema(
    operation_description='Obtener, actualizar o eliminar un producto..',
    responses={
        200: 'Success',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
    },
)
def product_list(request):
    """
    Obtener, actualizar o eliminar un producto...
    """
    if request.method == 'GET':
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos, many=True)
        return Response(productos_serializer.data)

    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Producto.objects.all().delete()
        return Response(
            {'mensaje': '{} productos han sido eliminados de la base de datos!'.format(cantidad[0])},
            status=status.HTTP_204_NO_CONTENT
        )



@api_view(['GET', 'PUT', 'DELETE'])
@swagger_auto_schema(
    operation_description='Obtener, actualizar o eliminar un producto.',
    responses={
        200: 'Success',
        202: 'Accepted',
        204: 'No Content',
        400: 'Bad Request',
        404: 'Not Found'
    },
)
def product_detail(request, product_id):
    """
    Obtener, actualizar o eliminar un producto..
    """
    try:
        producto = Producto.objects.get(idProducto=product_id)
    except:
        return Response({'mensaje': 'El producto no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        productos_serializer = ProductoSerializer(producto)
        return Response(productos_serializer.data)

    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(producto, data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(
            {'mensaje': 'El producto {} ha sido eliminado satisfactoriamente!'.format(product_id)},
            status=status.HTTP_204_NO_CONTENT
        )



@api_view(['GET'])
@swagger_auto_schema(
    operation_description='Lista todas las marcas de los instrumentos',
    responses={200: 'Success', 400: 'Bad Request'},
)
def marcas_list(request):
    """
    Lista todas las marcas de los instrumentos.
    """
    if request.method == 'GET':
        marcas = Marca.objects.all()
        marcas_serializer = MarcaSerializer(marcas, many=True)
        return Response(marcas_serializer.data)