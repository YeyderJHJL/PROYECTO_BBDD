from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import ProtectedError
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def estado_registro_list(request):
    estados = EstadoRegistro.objects.all()
    return render(request, 'estado_registro_list.html', {'estados': estados})

def estado_registro_create(request):
    if request.method == "POST":
        form = EstadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_registro_list')
    else:
        form = EstadoRegistroForm()
    return render(request, 'estado_registro_form.html', {'form': form})

def estado_registro_update(request, pk):
    estado = get_object_or_404(EstadoRegistro, pk=pk)
    if request.method == "POST":
        form = EstadoRegistroForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('estado_registro_list')
    else:
        form = EstadoRegistroForm(instance=estado)
    return render(request, 'estado_registro_form.html', {'form': form})

def estado_registro_delete(request, pk):
    estado = get_object_or_404(EstadoRegistro, pk=pk)
    if request.method == "POST":
        try:
            estado.delete()
            messages.success(request, "Estado de registro eliminado correctamente.")
            return redirect('estado_registro_list')
        except ProtectedError as e:
            related_objects = e.protected_objects
            related_details = []
            for obj in related_objects:
                model_name = obj._meta.verbose_name  
                obj_name = str(obj)  
                related_details.append(f"{obj_name} (En la tabla: {model_name})")
            messages.error(request, "No se puede eliminar este estado de registro porque está relacionado con otros registros.")
            return render(request, 'estado_registro_delete.html', {'estado': estado, 'related_details': related_details})
    else:
        return render(request, 'estado_registro_delete.html', {'estado': estado})

def tipo_cliente_list(request):
    tipos = TipoCliente.objects.all()
    return render(request, 'tipo_cliente_list.html', {'tipos': tipos})

def tipo_cliente_create(request):
    if request.method == "POST":
        form = TipoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_cliente_list')
    else:
        form = TipoClienteForm()
    return render(request, 'tipo_cliente_form.html', {'form': form})

def tipo_cliente_update(request, pk):
    tipo = get_object_or_404(TipoCliente, pk=pk)
    if request.method == "POST":
        form = TipoClienteForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipo_cliente_list')
    else:
        form = TipoClienteForm(instance=tipo)
    return render(request, 'tipo_cliente_form.html', {'form': form})

def tipo_cliente_delete(request, pk):
    tipo = get_object_or_404(TipoCliente, pk=pk)
    if request.method == "POST":
        try:
            tipo.delete()
            messages.success(request, "Tipo de cliente eliminado correctamente.")
            return redirect('tipo_cliente_list')
        except ProtectedError as e:
            related_objects = e.protected_objects
            related_details = []
            for obj in related_objects:
                model_name = obj._meta.verbose_name  
                obj_name = str(obj)  
                related_details.append(f"{obj_name} (En la tabla: {model_name})")
            messages.error(request, "No se puede eliminar este tipo de cliente porque está relacionado con otros registros.")
            return render(request, 'tipo_cliente_delete.html', {'tipo': tipo, 'related_details': related_details})
    else:
        return render(request, 'tipo_cliente_delete.html', {'tipo': tipo})
    
def estado_cliente_list(request):
    estados = EstadoCliente.objects.all()
    return render(request, 'estado_cliente_list.html', {'estados': estados})

def estado_cliente_create(request):
    if request.method == "POST":
        form = EstadoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_cliente_list')
    else:
        form = EstadoClienteForm()
    return render(request, 'estado_cliente_form.html', {'form': form})

def estado_cliente_update(request, pk):
    estado = get_object_or_404(EstadoCliente, pk=pk)
    if request.method == "POST":
        form = EstadoClienteForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('estado_cliente_list')
    else:
        form = EstadoClienteForm(instance=estado)
    return render(request, 'estado_cliente_form.html', {'form': form})

def estado_cliente_delete(request, pk):
    estado = get_object_or_404(EstadoCliente, pk=pk)
    if request.method == "POST":
        try:
            estado.delete()
            messages.success(request, "Estado de cliente eliminado correctamente.")
            return redirect('estado_cliente_list')
        except ProtectedError as e:
            related_objects = e.protected_objects
            related_details = []
            for obj in related_objects:
                model_name = obj._meta.verbose_name  
                obj_name = str(obj)  
                related_details.append(f"{obj_name} (En la tabla: {model_name})")
            messages.error(request, "No se puede eliminar este estado de cliente porque está relacionado con otros registros.")
            return render(request, 'estado_cliente_delete.html', {'estado': estado, 'related_details': related_details})
    else:
        return render(request, 'estado_cliente_delete.html', {'estado': estado})


def tipo_proyecto_list(request):
    tipos = TipoProyecto.objects.all()
    return render(request, 'tipo_proyecto_list.html', {'tipos': tipos})

def tipo_proyecto_create(request):
    if request.method == "POST":
        form = TipoProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_proyecto_list')
    else:
        form = TipoProyectoForm()
    return render(request, 'tipo_proyecto_form.html', {'form': form})

def tipo_proyecto_update(request, pk):
    tipo = get_object_or_404(TipoProyecto, pk=pk)
    if request.method == "POST":
        form = TipoProyectoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipo_proyecto_list')
    else:
        form = TipoProyectoForm(instance=tipo)
    return render(request, 'tipo_proyecto_form.html', {'form': form})

def tipo_proyecto_delete(request, pk):
    tipo = get_object_or_404(TipoProyecto, pk=pk)
    if request.method == "POST":
        tipo.delete()
        return redirect('tipo_proyecto_list')
    return render(request, 'tipo_proyecto_delete.html', {'tipo': tipo})

def estado_proyecto_list(request):
    estados_proyecto = EstadoProyecto.objects.all()
    return render(request, 'estado_proyecto_list.html', {'estados_proyecto': estados_proyecto})

def estado_proyecto_create(request):
    if request.method == "POST":
        form = EstadoProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_proyecto_list')
    else:
        form = EstadoProyectoForm()
    return render(request, 'estado_proyecto_form.html', {'form': form})

def estado_proyecto_update(request, pk):
    estado_proyecto = get_object_or_404(EstadoProyecto, pk=pk)
    if request.method == "POST":
        form = EstadoProyectoForm(request.POST, instance=estado_proyecto)
        if form.is_valid():
            form.save()
            return redirect('estado_proyecto_list')
    else:
        form = EstadoProyectoForm(instance=estado_proyecto)
    return render(request, 'estado_proyecto_form.html', {'form': form})

def estado_proyecto_delete(request, pk):
    estado_proyecto = get_object_or_404(EstadoProyecto, pk=pk)
    if request.method == "POST":
        estado_proyecto.delete()
        return redirect('estado_proyecto_list')
    return render(request, 'estado_proyecto_delete.html', {'estado_proyecto': estado_proyecto})

def etapas_proyecto_list(request):
    etapas = EtapasProyecto.objects.all()
    return render(request, 'etapas_proyecto_list.html', {'etapas': etapas})

def etapas_proyecto_create(request):
    if request.method == "POST":
        form = EtapasProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etapas_proyecto_list')
    else:
        form = EtapasProyectoForm()
    return render(request, 'etapas_proyecto_form.html', {'form': form})

def etapas_proyecto_update(request, pk):
    etapa = get_object_or_404(EtapasProyecto, pk=pk)
    if request.method == "POST":
        form = EtapasProyectoForm(request.POST, instance=etapa)
        if form.is_valid():
            form.save()
            return redirect('etapas_proyecto_list')
    else:
        form = EtapasProyectoForm(instance=etapa)
    return render(request, 'etapas_proyecto_form.html', {'form': form})

def etapas_proyecto_delete(request, pk):
    etapa = get_object_or_404(EtapasProyecto, pk=pk)
    if request.method == "POST":
        etapa.delete()
        return redirect('etapas_proyecto_list')
    return render(request, 'etapas_proyecto_delete.html', {'etapa': etapa})

def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividad_list.html', {'actividades': actividades})

def actividad_create(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm()
    return render(request, 'actividad_form.html', {'form': form})

def actividad_update(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividad_form.html', {'form': form})

def actividad_delete(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == "POST":
        actividad.delete()
        return redirect('actividad_list')
    return render(request, 'actividad_delete.html', {'actividad': actividad})

def complejidad_list(request):
    complejidades = Complejidad.objects.all()
    return render(request, 'complejidad_list.html', {'complejidades': complejidades})

def complejidad_create(request):
    if request.method == "POST":
        form = ComplejidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complejidad_list')
    else:
        form = ComplejidadForm()
    return render(request, 'complejidad_form.html', {'form': form})

def complejidad_update(request, pk):
    complejidad = get_object_or_404(Complejidad, pk=pk)
    if request.method == "POST":
        form = ComplejidadForm(request.POST, instance=complejidad)
        if form.is_valid():
            form.save()
            return redirect('complejidad_list')
    else:
        form = ComplejidadForm(instance=complejidad)
    return render(request, 'complejidad_form.html', {'form': form})

def complejidad_delete(request, pk):
    complejidad = get_object_or_404(Complejidad, pk=pk)
    if request.method == "POST":
        complejidad.delete()
        return redirect('complejidad_list')
    return render(request, 'complejidad_delete.html', {'complejidad': complejidad})

def cargosproyecto_list(request):
    cargos_proyecto = CargosProyecto.objects.all()
    return render(request, 'cargos_proyecto_list.html', {'cargos_proyecto': cargos_proyecto})

def cargosproyecto_create(request):
    if request.method == "POST":
        form = CargosProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargos_proyecto_list')
    else:
        form = CargosProyectoForm()
    return render(request, 'cargos_proyecto_form.html', {'form': form})

def cargosproyecto_update(request, pk):
    cargo_proyecto = get_object_or_404(CargosProyecto, pk=pk)
    if request.method == "POST":
        form = CargosProyectoForm(request.POST, instance=cargo_proyecto)
        if form.is_valid():
            form.save()
            return redirect('cargos_proyecto_list')
    else:
        form = CargosProyectoForm(instance=cargo_proyecto)
    return render(request, 'cargos_proyecto_form.html', {'form': form})

def cargosproyecto_delete(request, pk):
    cargo_proyecto = get_object_or_404(CargosProyecto, pk=pk)
    if request.method == "POST":
        cargo_proyecto.delete()
        return redirect('cargos_proyecto_list')
    return render(request, 'cargos_proyecto_delete.html', {'cargo_proyecto': cargo_proyecto})

def cargos_personal_list(request):
    cargos = CargosPersonal.objects.all()
    return render(request, 'cargos_personal_list.html', {'cargos': cargos})

def cargos_personal_create(request):
    if request.method == "POST":
        form = CargosPersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargos_personal_list')
    else:
        form = CargosPersonalForm()
    return render(request, 'cargos_personal_form.html', {'form': form})

def cargos_personal_update(request, pk):
    cargo = get_object_or_404(CargosPersonal, pk=pk)
    if request.method == "POST":
        form = CargosPersonalForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargos_personal_list')
    else:
        form = CargosPersonalForm(instance=cargo)
    return render(request, 'cargos_personal_form.html', {'form': form})

def cargos_personal_delete(request, pk):
    cargo = get_object_or_404(CargosPersonal, pk=pk)
    if request.method == "POST":
        cargo.delete()
        return redirect('cargos_personal_list')
    return render(request, 'cargos_personal_delete.html', {'cargo': cargo})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
        
    if request.method == "POST":
        try:
            cliente.delete()
            messages.success(request, "Cliente eliminado correctamente.")
            return redirect('cliente_list')
        except ProtectedError as e:
            related_objects = e.protected_objects
            related_details = []
            for obj in related_objects:
                model_name = obj._meta.verbose_name
                obj_name = str(obj)
                related_details.append(f"{obj_name} (En la tabla: {model_name})")
            messages.error(request, "No se puede eliminar este cliente porque está relacionado con otros registros.")
            return render(request, 'cliente_delete.html', {'cliente': cliente, 'related_details': related_details})
    else:
        return render(request, 'cliente_delete.html', {'cliente': cliente})