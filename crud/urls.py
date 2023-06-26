from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name='product-list'),
    path('new/',product_new,name='product-new'),
    path('<str:product_id>/', product_detail, name= 'product-detail'),
    path('<str:product_id>/edit', product_edit, name= 'product-edit'),
    path('<str:product_id>/delete', product_delete, name= 'product-delete'),
]
