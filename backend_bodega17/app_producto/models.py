from django.db import models

class CategoriaAlmacen(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField(blank=True, null=True)
    temperatura_ideal = models.CharField(max_length=50, blank=True, null=True)
    tipo_almacenamiento = models.CharField(max_length=50, blank=True, null=True)
    es_peligroso = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = "Categoría de Almacén"
        verbose_name_plural = "Categorías de Almacén"


class ProveedorAlmacen(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    contacto_persona = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    direccion_proveedor = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    pais_origen = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = "Proveedor de Almacén"
        verbose_name_plural = "Proveedores de Almacén"


class EmpleadoAlmacen(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    licencia_manejo_montacargas = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Empleado de Almacén"
        verbose_name_plural = "Empleados de Almacén"


class ProductoAlmacen(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    codigo_sku = models.CharField(max_length=50, unique=True)
    stock_actual = models.IntegerField()
    ubicacion_almacen = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaAlmacen, on_delete=models.SET_NULL, null=True, related_name='productos')
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.SET_NULL, null=True, related_name='productos')
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volumen_m3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_ultimo_movimiento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = "Producto de Almacén"
        verbose_name_plural = "Productos de Almacén"


class EntradaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE, related_name='entradas')
    cantidad_entrada = models.IntegerField()
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(ProveedorAlmacen, on_delete=models.SET_NULL, null=True, related_name='entradas')
    num_factura_compra = models.CharField(max_length=50)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    empleado_recepcion = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, related_name='entradas_recibidas')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Entrada de {self.cantidad_entrada} de {self.producto.nombre_producto}"

    class Meta:
        verbose_name = "Entrada de Producto"
        verbose_name_plural = "Entradas de Productos"


class SalidaProducto(models.Model):
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE, related_name='salidas')
    cantidad_salida = models.IntegerField()
    fecha_salida = models.DateTimeField(auto_now_add=True)
    destino = models.CharField(max_length=100)
    id_cliente_salida = models.IntegerField(blank=True, null=True)  # No Client table provided
    num_pedido_salida = models.CharField(max_length=50)
    empleado_despacho = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, related_name='salidas_despachadas')
    motivo_salida = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Salida de {self.cantidad_salida} de {self.producto.nombre_producto}"

    class Meta:
        verbose_name = "Salida de Producto"
        verbose_name_plural = "Salidas de Productos"


class InventarioFisico(models.Model):
    fecha_inventario = models.DateField()
    producto = models.ForeignKey(ProductoAlmacen, on_delete=models.CASCADE, related_name='inventarios')
    stock_sistema = models.IntegerField()
    stock_fisico = models.IntegerField()
    diferencia = models.IntegerField()
    empleado_realizo = models.ForeignKey(EmpleadoAlmacen, on_delete=models.SET_NULL, null=True, related_name='inventarios_realizados')
    comentarios = models.TextField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario de {self.producto.nombre_producto} el {self.fecha_inventario}"

    class Meta:
        verbose_name = "Inventario Físico"
        verbose_name_plural = "Inventarios Físicos"
