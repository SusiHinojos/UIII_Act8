from django import forms
from .models import CategoriaAlmacen, ProveedorAlmacen, EmpleadoAlmacen, ProductoAlmacen, EntradaProducto, SalidaProducto, InventarioFisico

class DateInput(forms.DateInput):
    input_type = 'date'

class CategoriaAlmacenForm(forms.ModelForm):
    class Meta:
        model = CategoriaAlmacen
        fields = '__all__'
        widgets = {
            'nombre_categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_categoria': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'temperatura_ideal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_almacenamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'es_peligroso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProveedorAlmacenForm(forms.ModelForm):
    class Meta:
        model = ProveedorAlmacen
        fields = '__all__'
        widgets = {
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'email_proveedor': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_proveedor': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class EmpleadoAlmacenForm(forms.ModelForm):
    class Meta:
        model = EmpleadoAlmacen
        fields = '__all__'
        widgets = {
            'nombre_empleado': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_empleado': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratacion': DateInput(attrs={'class': 'form-control'}),
            'email_empleado': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_empleado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoAlmacenForm(forms.ModelForm):
    class Meta:
        model = ProductoAlmacen
        fields = ['nombre_producto', 'descripcion', 'codigo_sku', 'stock_actual', 'ubicacion_almacen', 'categoria', 'proveedor', 'peso_kg', 'volumen_m3']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'codigo_sku': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_actual': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion_almacen': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'categoria'
            'proveedor': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'proveedor'
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'volumen_m3': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EntradaProductoForm(forms.ModelForm):
    class Meta:
        model = EntradaProducto
        fields = ['producto', 'cantidad_entrada', 'proveedor', 'num_factura_compra', 'costo_unitario', 'empleado_recepcion', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'producto'
            'cantidad_entrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'proveedor'
            'num_factura_compra': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'empleado_recepcion': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'empleado_recepcion'
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class SalidaProductoForm(forms.ModelForm):
    class Meta:
        model = SalidaProducto
        fields = ['producto', 'cantidad_salida', 'destino', 'id_cliente_salida', 'num_pedido_salida', 'empleado_despacho', 'motivo_salida']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'producto'
            'cantidad_salida': forms.NumberInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'id_cliente_salida': forms.TextInput(attrs={'class': 'form-control'}),
            'num_pedido_salida': forms.TextInput(attrs={'class': 'form-control'}),
            'empleado_despacho': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'empleado_despacho'
            'motivo_salida': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class InventarioFisicoForm(forms.ModelForm):
    class Meta:
        model = InventarioFisico
        fields = ['fecha_inventario', 'producto', 'stock_sistema', 'stock_fisico', 'empleado_realizo', 'comentarios']
        widgets = {
            'fecha_inventario': DateInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'producto'
            'stock_sistema': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_fisico': forms.NumberInput(attrs={'class': 'form-control'}),
            'empleado_realizo': forms.Select(attrs={'class': 'form-select'}),  # Corrected the Select widget for 'empleado_realizo'
            'comentarios': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        stock_sistema = cleaned_data.get("stock_sistema")
        stock_fisico = cleaned_data.get("stock_fisico")

        if stock_sistema is not None and stock_fisico is not None:
            cleaned_data['diferencia'] = stock_fisico - stock_sistema
        
        return cleaned_data
