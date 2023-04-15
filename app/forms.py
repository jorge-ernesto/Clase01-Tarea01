from django import forms
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Se puede usar tuplas o listas
LISTA_CARGO = (
    ("Soporte", "Soporte"),
    ("Desarrollo", "Desarrollo"),
    ("Lider Tecnico", "Lider Tecnico"),
    ("Vendedor", "Vendedor"),
    ("Jefe de Operaciones", "Jefe de Operaciones"),
    ("Gerente General", "Gerente General"),
)

LISTA_AREA = (
    ("Soporte", "Soporte"),
    ("Desarrollo", "Desarrollo"),
    ("Ventas", "Ventas"),
    ("Operaciones", "Operaciones"),
    ("Gerencia", "Gerencia"),
)

class Empleado(forms.Form):
    # Definir los datos de la clase (inputs del formulario)
    # Si no se especifica lo contrario, todos los inputs seran required=TRUE por defecto
    codigo = forms.CharField()
    nombre = forms.CharField()

    # Validar que el input "fecha_ingreso" sea tipo date y required (Aunque ya lo es por defecto)
    fecha_ingreso = forms.DateField(
        widget = forms.DateInput(attrs={'type': 'date'}),
        required = True
    )

    cargo = forms.ChoiceField(choices=LISTA_CARGO)
    area = forms.ChoiceField(choices=LISTA_AREA)
    sueldo_total = forms.IntegerField()

    # Validar que el input "descuento" no sea menor que 0 y mayor que 100 (Puede ir entre 0 y 100)
    descuento = forms.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(100)]
    )

    # Validar que el input "sueldo_neto" este deshabilitado y no sea requerido (Esta cantidad se calculara en las views)
    sueldo_neto = forms.IntegerField(
        widget = forms.TextInput(attrs={'disabled': 'disabled'}),
        required = False
    )
