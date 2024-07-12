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
    

def actividades_complejidad_list(request):
    actividades_complejidad = ActividadesComplejidad.objects.all()
    return render(request, 'actividades_complejidad_list.html', {'actividades_complejidad': actividades_complejidad})

def actividades_complejidad_create(request):
    if request.method == "POST":
        form = ActividadesComplejidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividades_complejidad_list')
    else:
        form = ActividadesComplejidadForm()
    return render(request, 'actividades_complejidad_form.html', {'form': form})

def actividades_complejidad_update(request, pk):
    actividad_complejidad = get_object_or_404(ActividadesComplejidad, pk=pk)
    if request.method == "POST":
        form = ActividadesComplejidadForm(request.POST, instance=actividad_complejidad)
        if form.is_valid():
            form.save()
            return redirect('actividades_complejidad_list')
    else:
        form = ActividadesComplejidadForm(instance=actividad_complejidad)
    return render(request, 'actividades_complejidad_form.html', {'form': form})

def actividades_complejidad_delete(request, pk):
    actividad_complejidad = get_object_or_404(ActividadesComplejidad, pk=pk)
    if request.method == "POST":
        actividad_complejidad.delete()
        return redirect('actividades_complejidad_list')
    return render(request, 'actividades_complejidad_delete.html', {'actividad_complejidad': actividad_complejidad})

# Etapa Actividad
def etapa_actividad_list(request):
    etapas_actividad = EtapaActividad.objects.all()
    return render(request, 'etapa_actividad_list.html', {'etapas_actividad': etapas_actividad})

def etapa_actividad_create(request):
    if request.method == "POST":
        form = EtapaActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etapa_actividad_list')
    else:
        form = EtapaActividadForm()
    return render(request, 'etapa_actividad_form.html', {'form': form})

def etapa_actividad_update(request, pk):
    etapa_actividad = get_object_or_404(EtapaActividad, pk=pk)
    if request.method == "POST":
        form = EtapaActividadForm(request.POST, instance=etapa_actividad)
        if form.is_valid():
            form.save()
            return redirect('etapa_actividad_list')
    else:
        form = EtapaActividadForm(instance=etapa_actividad)
    return render(request, 'etapa_actividad_form.html', {'form': form})

def etapa_actividad_delete(request, pk):
    etapa_actividad = get_object_or_404(EtapaActividad, pk=pk)
    if request.method == "POST":
        etapa_actividad.delete()
        return redirect('etapa_actividad_list')
    return render(request, 'etapa_actividad_delete.html', {'etapa_actividad': etapa_actividad})

# Incidencia Personal
def incidencia_personal_list(request):
    incidencias_personal = IncidenciaPersonal.objects.all()
    return render(request, 'incidencia_personal_list.html', {'incidencias_personal': incidencias_personal})

def incidencia_personal_create(request):
    if request.method == "POST":
        form = IncidenciaPersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidencia_personal_list')
    else:
        form = IncidenciaPersonalForm()
    return render(request, 'incidencia_personal_form.html', {'form': form})

def incidencia_personal_update(request, pk):
    incidencia_personal = get_object_or_404(IncidenciaPersonal, pk=pk)
    if request.method == "POST":
        form = IncidenciaPersonalForm(request.POST, instance=incidencia_personal)
        if form.is_valid():
            form.save()
            return redirect('incidencia_personal_list')
    else:
        form = IncidenciaPersonalForm(instance=incidencia_personal)
    return render(request, 'incidencia_personal_form.html', {'form': form})

def incidencia_personal_delete(request, pk):
    incidencia_personal = get_object_or_404(IncidenciaPersonal, pk=pk)
    if request.method == "POST":
        incidencia_personal.delete()
        return redirect('incidencia_personal_list')
    return render(request, 'incidencia_personal_delete.html', {'incidencia_personal': incidencia_personal})

# Incidencias
def incidencias_list(request):
    incidencias = Incidencias.objects.all()
    return render(request, 'incidencias_list.html', {'incidencias': incidencias})

def incidencias_create(request):
    if request.method == "POST":
        form = IncidenciasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidencias_list')
    else:
        form = IncidenciasForm()
    return render(request, 'incidencias_form.html', {'form': form})

def incidencias_update(request, pk):
    incidencia = get_object_or_404(Incidencias, pk=pk)
    if request.method == "POST":
        form = IncidenciasForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('incidencias_list')
    else:
        form = IncidenciasForm(instance=incidencia)
    return render(request, 'incidencias_form.html', {'form': form})

def incidencias_delete(request, pk):
    incidencia = get_object_or_404(Incidencias, pk=pk)
    if request.method == "POST":
        incidencia.delete()
        return redirect('incidencias_list')
    return render(request, 'incidencias_delete.html', {'incidencia': incidencia})

# Personal
def personal_list(request):
    personal = Personal.objects.all()
    return render(request, 'personal_list.html', {'personal': personal})

def personal_create(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'personal_form.html', {'form': form})

def personal_update(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'personal_form.html', {'form': form})

def personal_delete(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == "POST":
        personal.delete()
        return redirect('personal_list')
    return render(request, 'personal_delete.html', {'personal': personal})

# Personal Actividad
def personal_actividad_list(request):
    personal_actividades = PersonalActividad.objects.all()
    return render(request, 'personal_actividad_list.html', {'personal_actividades': personal_actividades})

def personal_actividad_create(request):
    if request.method == "POST":
        form = PersonalActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_actividad_list')
    else:
        form = PersonalActividadForm()
    return render(request, 'personal_actividad_form.html', {'form': form})

def personal_actividad_update(request, pk):
    personal_actividad = get_object_or_404(PersonalActividad, pk=pk)
    if request.method == "POST":
        form = PersonalActividadForm(request.POST, instance=personal_actividad)
        if form.is_valid():
            form.save()
            return redirect('personal_actividad_list')
    else:
        form = PersonalActividadForm(instance=personal_actividad)
    return render(request, 'personal_actividad_form.html', {'form': form})

def personal_actividad_delete(request, pk):
    personal_actividad = get_object_or_404(PersonalActividad, pk=pk)
    if request.method == "POST":
        personal_actividad.delete()
        return redirect('personal_actividad_list')
    return render(request, 'personal_actividad_delete.html', {'personal_actividad': personal_actividad})

# Personal Cargos Personal
def personal_cargos_personal_list(request):
    personal_cargos = PersonalCargosPersonal.objects.all()
    return render(request, 'personal_cargos_personal_list.html', {'personal_cargos': personal_cargos})

def personal_cargos_personal_create(request):
    if request.method == "POST":
        form = PersonalCargosPersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_cargos_personal_list')
    else:
        form = PersonalCargosPersonalForm()
    return render(request, 'personal_cargos_personal_form.html', {'form': form})

def personal_cargos_personal_update(request, pk):
    personal_cargo = get_object_or_404(PersonalCargosPersonal, pk=pk)
    if request.method == "POST":
        form = PersonalCargosPersonalForm(request.POST, instance=personal_cargo)
        if form.is_valid():
            form.save()
            return redirect('personal_cargos_personal_list')
    else:
        form = PersonalCargosPersonalForm(instance=personal_cargo)
    return render(request, 'personal_cargos_personal_form.html', {'form': form})

def personal_cargos_personal_delete(request, pk):
    personal_cargo = get_object_or_404(PersonalCargosPersonal, pk=pk)
    if request.method == "POST":
        personal_cargo.delete()
        return redirect('personal_cargos_personal_list')
    return render(request, 'personal_cargos_personal_delete.html', {'personal_cargo': personal_cargo})

# Personal Cargos Proyecto
def personal_cargos_proyecto_list(request):
    personal_cargos_proyecto = PersonalCargosProyecto.objects.all()
    return render(request, 'personal_cargos_proyecto_list.html', {'personal_cargos_proyecto': personal_cargos_proyecto})

def personal_cargos_proyecto_create(request):
    if request.method == "POST":
        form = PersonalCargosProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_cargos_proyecto_list')
    else:
        form = PersonalCargosProyectoForm()
    return render(request, 'personal_cargos_proyecto_form.html', {'form': form})

def personal_cargos_proyecto_update(request, pk):
    personal_cargo_proyecto = get_object_or_404(PersonalCargosProyecto, pk=pk)
    if request.method == "POST":
        form = PersonalCargosProyectoForm(request.POST, instance=personal_cargo_proyecto)
        if form.is_valid():
            form.save()
            return redirect('personal_cargos_proyecto_list')
    else:
        form = PersonalCargosProyectoForm(instance=personal_cargo_proyecto)
    return render(request, 'personal_cargos_proyecto_form.html', {'form': form})

def personal_cargos_proyecto_delete(request, pk):
    personal_cargo_proyecto = get_object_or_404(PersonalCargosProyecto, pk=pk)
    if request.method == "POST":
        personal_cargo_proyecto.delete()
        return redirect('personal_cargos_proyecto_list')
    return render(request, 'personal_cargos_proyecto_delete.html', {'personal_cargo_proyecto': personal_cargo_proyecto})

# Proyecto
def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})

def proyecto_create(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto_form.html', {'form': form})

def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyecto_form.html', {'form': form})

def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'proyecto_delete.html', {'proyecto': proyecto})

def actividad_list(request):
    actividades = Actividad.objects.all()
    complejidades = Complejidad.objects.all()
    return render(request, 'actividad_list.html', {'actividades': actividades, 'complejidades': complejidades})

def actividad_create(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save()
            if form.cleaned_data['complejidad']:
                ActividadesComplejidad.objects.create(actcod=actividad, comcod=form.cleaned_data['complejidad'])
            return redirect('actividad_list')
    else:
        form = ActividadForm()
    return render(request, 'actividad_form.html', {'form': form})   

def actividad_update(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            actividad = form.save()
            if form.cleaned_data['complejidad']:
                ActividadesComplejidad.objects.update_or_create(actcod=actividad, defaults={'comcod': form.cleaned_data['complejidad']})
            return redirect('actividad_list')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividad_form.html', {'form': form})

def actividad_delete(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == 'POST':
        actividad.delete()
        return redirect('actividad_list')
    return render(request, 'actividad_delete.html', {'actividad': actividad})

def complejidad_create(request):
    if request.method == 'POST':
        form = ComplejidadForm(request.POST)
        if form.is_valid():
            complejidad = form.save()
            if form.cleaned_data['actividad']:
                ActividadesComplejidad.objects.create(comcod=complejidad, actcod=form.cleaned_data['actividad'])
            return redirect('actividad_list')
    else:
        form = ComplejidadForm()
    return render(request, 'complejidad_form.html', {'form': form})

def complejidad_update(request, pk):
    complejidad = get_object_or_404(Complejidad, pk=pk)
    if request.method == 'POST':
        form = ComplejidadForm(request.POST, instance=complejidad)
        if form.is_valid():
            complejidad = form.save()
            if form.cleaned_data['actividad']:
                ActividadesComplejidad.objects.update_or_create(comcod=complejidad, defaults={'actcod': form.cleaned_data['actividad']})
            return redirect('actividad_list')
    else:
        form = ComplejidadForm(instance=complejidad)
    return render(request, 'complejidad_form.html', {'form': form})

def complejidad_delete(request, pk):
    complejidad = get_object_or_404(Complejidad, pk=pk)
    if request.method == 'POST':
        complejidad.delete()
        return redirect('actividad_list')
    return render(request, 'complejidad_delete.html', {'complejidad': complejidad})
