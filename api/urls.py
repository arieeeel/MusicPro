from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('productos/',product_list),
    path('productos/<str:product_id>',product_detail),
    path('marcas/',marcas_list),
    path('saludo/',saludo),
    path('saldo/',saldo),
    path('bodega/',views.bodega),
    path('seguimiento/',transporte),

]