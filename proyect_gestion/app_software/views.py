from django.shortcuts import render, get_object_or_404, redirect
from .models import EstadoRegistro
from .forms import EstadoRegistroForm

# Create your views here.

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
        estado.delete()
        return redirect('estado_registro_list')
    return render(request, 'estado_registro_delete.html', {'estado': estado})
