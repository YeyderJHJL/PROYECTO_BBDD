from django import forms
from .models import *

class EstadoRegistroForm(forms.ModelForm):
    class Meta:
        model = EstadoRegistro
        fields = ['estregnom', 'estregestreg']
        widgets = {
            'estregnom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoClienteForm(forms.ModelForm):
    class Meta:
        model = TipoCliente
        fields = ['tipclinom', 'estregcod']
        widgets = {
            'tipclinom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class EstadoClienteForm(forms.ModelForm):
    class Meta:
        model = EstadoCliente
        fields = ['estclinom', 'estregcod']
        widgets = {
            'estclinom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class TipoProyectoForm(forms.ModelForm):
    class Meta:
        model = TipoProyecto
        fields = ['tippronom', 'estregcod']
        widgets = {
            'tippronom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class EstadoProyectoForm(forms.ModelForm):
    class Meta:
        model = EstadoProyecto
        fields = ['estpronom', 'estregcod']
        widgets = {
            'estpronom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class EtapasProyectoForm(forms.ModelForm):
    class Meta:
        model = EtapasProyecto
        fields = ['etapronom', 'etaprofecreg', 'etaprofecini', 'etaprofecfin', 'estregcod']
        widgets = {
            'etapronom': forms.TextInput(attrs={'class': 'form-control'}),
            'etaprofecreg': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'etaprofecini': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'etaprofecfin': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['actnom', 'actfecini', 'actfecfin', 'acttip', 'acthortradia', 'estregcod']
        widgets = {
            'actnom': forms.TextInput(attrs={'class': 'form-control'}),
            'actfecini': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'actfecfin': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'acttip': forms.TextInput(attrs={'class': 'form-control'}),
            'acthortradia': forms.TimeInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class ComplejidadForm(forms.ModelForm):
    class Meta:
        model = Complejidad
        fields = ['comnom', 'comgra', 'estregcod']
        widgets = {
            'comnom': forms.TextInput(attrs={'class': 'form-control'}),
            'comgra': forms.NumberInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class CargosProyectoForm(forms.ModelForm):
    class Meta:
        model = CargosProyecto
        fields = ['carpronom', 'prosec', 'estregcod']
        widgets = {
            'carpronom': forms.TextInput(attrs={'class': 'form-control'}),
            'prosec': forms.Select(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class CargosPersonalForm(forms.ModelForm):
    class Meta:
        model = CargosPersonal
        fields = ['carpernom', 'estregcod']
        widgets = {
            'carpernom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['clidni', 'clinom', 'clifecing', 'clifecces', 'clifecultprocer', 'clitipcod', 'cliestcod', 'regestcod']
        widgets = {
            'clidni': forms.NumberInput(attrs={'class': 'form-control'}),
            'clinom': forms.TextInput(attrs={'class': 'form-control'}),
            'clifecing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'clifecces': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'clifecultprocer': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'clitipcod': forms.Select(attrs={'class': 'form-control'}),
            'cliestcod': forms.Select(attrs={'class': 'form-control'}),
            'regestcod': forms.Select(attrs={'class': 'form-control'}),
        }
