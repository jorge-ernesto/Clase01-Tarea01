from django.shortcuts import render
from .forms import Empleado

# Create your views here.


def registrar(request):
    if request.method == "POST":
        # crear objeto de la clase empleado
        form = Empleado(request.POST)
        if form.is_valid():
            # asignar valores a la variables
            codigo = form.cleaned_data["codigo"]
            nombre = form.cleaned_data["nombre"]
            fecha_ingreso = form.cleaned_data["fecha_ingreso"]
            cargo = form.cleaned_data["cargo"]
            area = form.cleaned_data["area"]
            sueldo_total = form.cleaned_data["sueldo_total"]
            descuento = form.cleaned_data["descuento"]
            sueldo_neto = form.cleaned_data["sueldo_neto"]
            # procesar
            if sueldo_total > 1800:
                descuento = 10
            sueldo_neto = sueldo_total - (sueldo_total * (descuento/100))
            contexto = {"codigo": codigo, "nombre": nombre, "fecha_ingreso": fecha_ingreso,
                        "cargo": cargo, "area": area, "sueldo_total": sueldo_total, "descuento": descuento, "sueldo_neto": sueldo_neto}
            return render(request, "app/boleta.html", contexto)
    else:
        # crear objeto de la clase Empleado
        form = Empleado()
    contexto = {"form": form}
    return render(request, "app/registrar.html", contexto)
