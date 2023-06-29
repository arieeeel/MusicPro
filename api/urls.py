from django.urls import path, include
from .views import *


urlpatterns = [
    path('productos/',product_list),
    path('productos/<str:product_id>',product_detail),
    path('marcas/',marcas_list),
    path('saludo/',saludo),
    path('saldo/',saldo),
    path('producto/',getbodega),
    path('seguimiento/',transporte),

]