from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Categorias
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('ver_categorias/', views.ver_categorias, name='ver_categorias'),
    path('actualizar_categoria/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('borrar_categoria/<int:id>/', views.borrar_categoria, name='borrar_categoria'),
    # Empleados
    path('ver_empleados/', views.ver_empleados, name='ver_empleados'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('borrar_empleado/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    # Proveedores
    path('ver_proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
    # Productos
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('borrar_producto/<int:id>/', views.borrar_producto, name='borrar_producto'),
    # Entradas de Productos
    path('ver_entradas/', views.ver_entradas, name='ver_entradas'),
    path('agregar_entrada/', views.agregar_entrada, name='agregar_entrada'),
    path('actualizar_entrada/<int:id>/', views.actualizar_entrada, name='actualizar_entrada'),
    path('borrar_entrada/<int:id>/', views.borrar_entrada, name='borrar_entrada'),
    # Salidas de Productos
    path('ver_salidas/', views.ver_salidas, name='ver_salidas'),
    path('agregar_salida/', views.agregar_salida, name='agregar_salida'),
    path('actualizar_salida/<int:id>/', views.actualizar_salida, name='actualizar_salida'),
    path('borrar_salida/<int:id>/', views.borrar_salida, name='borrar_salida'),
    # Inventario Físico
    path('ver_inventarios/', views.ver_inventarios, name='ver_inventarios'),
    path('agregar_inventario/', views.agregar_inventario, name='agregar_inventario'),
    path('actualizar_inventario/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
    path('borrar_inventario/<int:id>/', views.borrar_inventario, name='borrar_inventario'),
]