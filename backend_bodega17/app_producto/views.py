from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoriaAlmacen, EmpleadoAlmacen, ProveedorAlmacen, ProductoAlmacen, EntradaProducto, SalidaProducto, InventarioFisico
from .forms import CategoriaAlmacenForm, ProveedorAlmacenForm, EmpleadoAlmacenForm, ProductoAlmacenForm, EntradaProductoForm, SalidaProductoForm, InventarioFisicoForm

def inicio(request):
    return render(request, 'inicio.html')

# Vistas para CategoriaAlmacen
def ver_categorias(request):
    categorias = CategoriaAlmacen.objects.all()
    return render(request, 'categoria_almacen/ver_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaAlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_categorias')
    else:
        form = CategoriaAlmacenForm()
    return render(request, 'categoria_almacen/agregar_categoria.html', {'form': form})

def actualizar_categoria(request, id):
    categoria = get_object_or_404(CategoriaAlmacen, pk=id)
    if request.method == 'POST':
        form = CategoriaAlmacenForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('ver_categorias')
    else:
        form = CategoriaAlmacenForm(instance=categoria)
    return render(request, 'categoria_almacen/actualizar_categoria.html', {'form': form, 'categoria': categoria})

def borrar_categoria(request, id):
    categoria = get_object_or_404(CategoriaAlmacen, pk=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria_almacen/borrar_categoria.html', {'categoria': categoria})

# Vistas para EmpleadoAlmacen
def ver_empleados(request):
    empleados = EmpleadoAlmacen.objects.all()
    return render(request, 'empleado_almacen/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoAlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoAlmacenForm()
    return render(request, 'empleado_almacen/agregar_empleado.html', {'form': form})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(EmpleadoAlmacen, pk=id)
    if request.method == 'POST':
        form = EmpleadoAlmacenForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('ver_empleados')
    else:
        form = EmpleadoAlmacenForm(instance=empleado)
    return render(request, 'empleado_almacen/actualizar_empleado.html', {'form': form, 'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(EmpleadoAlmacen, pk=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado_almacen/borrar_empleado.html', {'empleado': empleado})

# Vistas para ProveedorAlmacen
def ver_proveedores(request):
    proveedores = ProveedorAlmacen.objects.all()
    return render(request, 'proveedor_almacen/ver_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorAlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_proveedores')
    else:
        form = ProveedorAlmacenForm()
    return render(request, 'proveedor_almacen/agregar_proveedor.html', {'form': form})

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(ProveedorAlmacen, pk=id)
    if request.method == 'POST':
        form = ProveedorAlmacenForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('ver_proveedores')
    else:
        form = ProveedorAlmacenForm(instance=proveedor)
    return render(request, 'proveedor_almacen/actualizar_proveedor.html', {'form': form, 'proveedor': proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(ProveedorAlmacen, pk=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor_almacen/borrar_proveedor.html', {'proveedor': proveedor})

# Vistas para ProductoAlmacen
def ver_productos(request):
    productos = ProductoAlmacen.objects.select_related('categoria', 'proveedor').all()
    return render(request, 'producto_almacen/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    categorias = CategoriaAlmacen.objects.all()
    proveedores = ProveedorAlmacen.objects.all()
    if request.method == 'POST':
        form = ProductoAlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductoAlmacenForm()
    return render(request, 'producto_almacen/agregar_producto.html', {'form': form, 'categorias': categorias, 'proveedores': proveedores})

def actualizar_producto(request, id):
    categorias = CategoriaAlmacen.objects.all()
    proveedores = ProveedorAlmacen.objects.all()
    producto = get_object_or_404(ProductoAlmacen, pk=id)
    if request.method == 'POST':
        form = ProductoAlmacenForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductoAlmacenForm(instance=producto)
    return render(request, 'producto_almacen/actualizar_producto.html', {'form': form, 'producto': producto, 'categorias': categorias, 'proveedores': proveedores})

def borrar_producto(request, id):
    producto = get_object_or_404(ProductoAlmacen, pk=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto_almacen/borrar_producto.html', {'producto': producto})

# Vistas para EntradaProducto
def ver_entradas(request):
    entradas = EntradaProducto.objects.select_related('producto', 'proveedor', 'empleado_recepcion').all()
    return render(request, 'entrada_producto/ver_entradas.html', {'entradas': entradas})

def agregar_entrada(request):
    productos = ProductoAlmacen.objects.all()
    empleados = EmpleadoAlmacen.objects.all()
    proveedores = ProveedorAlmacen.objects.all()
    if request.method == 'POST':
        form = EntradaProductoForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.producto.stock_actual += entrada.cantidad_entrada
            entrada.producto.save()
            entrada.save()
            return redirect('ver_entradas')
    else:
        form = EntradaProductoForm()
    return render(request, 'entrada_producto/agregar_entrada.html', {'form': form, 'empleados':empleados, 'productos': productos, 'proveedores': proveedores})

def actualizar_entrada(request, id):
    entrada = get_object_or_404(EntradaProducto, pk=id)
    producto_original = entrada.producto
    cantidad_original = entrada.cantidad_entrada

    if request.method == 'POST':
        form = EntradaProductoForm(request.POST, instance=entrada)
        if form.is_valid():
            # Revertir el stock del producto original
            producto_original.stock_actual -= cantidad_original
            producto_original.save()

            # Actualizar la entrada y el stock del nuevo producto
            nueva_entrada = form.save()
            nuevo_producto = nueva_entrada.producto
            nuevo_producto.stock_actual += nueva_entrada.cantidad_entrada
            nuevo_producto.save()

            return redirect('ver_entradas')
    else:
        form = EntradaProductoForm(instance=entrada)
    
    productos = ProductoAlmacen.objects.all()
    empleados = EmpleadoAlmacen.objects.all()
    proveedores = ProveedorAlmacen.objects.all()
    return render(request, 'entrada_producto/actualizar_entrada.html', {'form': form, 'entrada': entrada, 'empleados':empleados, 'productos': productos, 'proveedores': proveedores})


def borrar_entrada(request, id):
    entrada = get_object_or_404(EntradaProducto, pk=id)
    if request.method == 'POST':
        entrada.producto.stock_actual -= entrada.cantidad_entrada
        entrada.producto.save()
        entrada.delete()
        return redirect('ver_entradas')
    return render(request, 'entrada_producto/borrar_entrada.html', {'entrada': entrada})

# Vistas para SalidaProducto
def ver_salidas(request):
    salidas = SalidaProducto.objects.select_related('producto', 'empleado_despacho').all()
    return render(request, 'salida_producto/ver_salidas.html', {'salidas': salidas})

def agregar_salida(request):
    productos = ProductoAlmacen.objects.all()
    empleados = EmpleadoAlmacen.objects.all()
    if request.method == 'POST':
        form = SalidaProductoForm(request.POST)
        if form.is_valid():
            salida = form.save(commit=False)
            producto = salida.producto
            if producto.stock_actual < salida.cantidad_salida:
                form.add_error('cantidad_salida', f'Stock insuficiente. Disponible: {producto.stock_actual}')
                return render(request, 'salida_producto/agregar_salida.html', {'form': form, 'productos': productos, 'empleados': empleados})
            else:
                producto.stock_actual -= salida.cantidad_salida
                producto.save()
                salida.save()
                return redirect('ver_salidas')
    else:
        form = SalidaProductoForm()
    return render(request, 'salida_producto/agregar_salida.html', {'form': form, 'empleados':empleados, 'productos': productos})

def actualizar_salida(request, id):
    salida = get_object_or_404(SalidaProducto, pk=id)
    producto_original = salida.producto
    cantidad_original = salida.cantidad_salida

    if request.method == 'POST':
        form = SalidaProductoForm(request.POST, instance=salida)
        if form.is_valid():
            # Revertir el stock del producto original
            producto_original.stock_actual += cantidad_original
            producto_original.save()

            # Actualizar la salida y el stock del nuevo producto
            nueva_salida = form.save(commit=False)
            nuevo_producto = nueva_salida.producto
            cantidad_nueva = nueva_salida.cantidad_salida

            if nuevo_producto.stock_actual < cantidad_nueva:
                form.add_error('cantidad_salida', f'Stock insuficiente. Disponible: {nuevo_producto.stock_actual}')
                # Revertir el cambio si el stock es insuficiente
                producto_original.stock_actual -= cantidad_original
                producto_original.save()
                return render(request, 'salida_producto/actualizar_salida.html', {'form': form, 'salida': salida})
            else:
                nuevo_producto.stock_actual -= cantidad_nueva
                nuevo_producto.save()
                nueva_salida.save()
                return redirect('ver_salidas')
    else:
        form = SalidaProductoForm(instance=salida)

    productos = ProductoAlmacen.objects.all()
    empleados = EmpleadoAlmacen.objects.all()
    return render(request, 'salida_producto/actualizar_salida.html', {'form': form, 'salida': salida, 'empleados':empleados, 'productos': productos})

def borrar_salida(request, id):
    salida = get_object_or_404(SalidaProducto, pk=id)
    if request.method == 'POST':
        salida.producto.stock_actual += salida.cantidad_salida
        salida.producto.save()
        salida.delete()
        return redirect('ver_salidas')
    return render(request, 'salida_producto/borrar_salida.html', {'salida': salida})

# Vistas para InventarioFisico
def ver_inventarios(request):
    inventarios = InventarioFisico.objects.select_related('producto', 'empleado_realizo').all()
    return render(request, 'inventario_fisico/ver_inventarios.html', {'inventarios': inventarios})

def agregar_inventario(request):
    if request.method == 'POST':
        form = InventarioFisicoForm(request.POST)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.diferencia = inventario.stock_fisico - inventario.stock_sistema
            inventario.save()
            return redirect('ver_inventarios')
    else:
        form = InventarioFisicoForm()
    return render(request, 'inventario_fisico/agregar_inventario.html', {'form': form})

def actualizar_inventario(request, id):
    inventario = get_object_or_404(InventarioFisico, pk=id)
    if request.method == 'POST':
        form = InventarioFisicoForm(request.POST, instance=inventario)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.diferencia = inventario.stock_fisico - inventario.stock_sistema
            inventario.save()
            return redirect('ver_inventarios')
    else:
        form = InventarioFisicoForm(instance=inventario)
    return render(request, 'inventario_fisico/actualizar_inventario.html', {'form': form, 'inventario': inventario})

def borrar_inventario(request, id):
    inventario = get_object_or_404(InventarioFisico, pk=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('ver_inventarios')
    return render(request, 'inventario_fisico/borrar_inventario.html', {'inventario': inventario})
