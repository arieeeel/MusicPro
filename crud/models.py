from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='ID')
    marca = models.CharField(max_length=50, verbose_name='Marca')

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'
        ordering=['idMarca']

    def __str__(self):
        return self.marca


class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['idProducto']

    def __str__(self):
        return self.descripcion
class Producto_Api(models.Model):
    idProductoApi = models.CharField(primary_key=True,max_length=20, verbose_name='ID')
    codigo = models.CharField(max_length=100,verbose_name='Codigo')
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    descripcion = models.CharField(max_length=300,verbose_name='Descripcion')
    producto_imagen = models.ImageField(upload_to='media/productosApi',null=True, blank=True)
    precio = models.CharField(max_length=300,verbose_name='Precio')
    precio_raw = models.CharField(max_length=300,verbose_name='Precio-Raw')
    asset = models.CharField(max_length=300,verbose_name='Asset')
    asset_raw = models.CharField(max_length=300,verbose_name='Asset-Raw')
    estado = models.CharField(max_length=300,verbose_name='estado')
    class Meta:
        verbose_name='productoApi'
        verbose_name_plural='productosApi'
        ordering=['idProductoApi']

    def __str__(self):
        return self.descripcion