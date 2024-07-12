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

    def clean_clidni(self):
        clidni = self.cleaned_data['clidni']
        #Asegurarnos que el DNI no se repita
        if Cliente.objects.filter(clidni=clidni).exists():
            raise forms.ValidationError("Error: Este DNI ya está registrado.")
        return clidni

class ActividadesComplejidadForm(forms.ModelForm):
    class Meta:
        model = ActividadesComplejidad
        fields = ['actcod', 'comcod']
        widgets = {
            'actcod': forms.Select(attrs={'class': 'form-control'}),
            'comcod': forms.Select(attrs={'class': 'form-control'}),
        }


class EtapaActividadForm(forms.ModelForm):
    class Meta:
        model = EtapaActividad
        fields = ['actcod', 'etaprocod']
        widgets = {
            'actcod': forms.Select(attrs={'class': 'form-control'}),
            'etaprocod': forms.Select(attrs={'class': 'form-control'}),
        }

class IncidenciaPersonalForm(forms.ModelForm):
    class Meta:
        model = IncidenciaPersonal
        fields = ['inccod', 'percod']
        widgets = {
            'inccod': forms.Select(attrs={'class': 'form-control'}),
            'percod': forms.Select(attrs={'class': 'form-control'}),
        }

class IncidenciasForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ['incfecini', 'incnom', 'incfecfin', 'incdes', 'actcod']
        widgets = {
            'incfecini': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'incnom': forms.TextInput(attrs={'class': 'form-control'}),
            'incfecfin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'incdes': forms.Textarea(attrs={'class': 'form-control'}),
            'actcod': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['pernom', 'percarcoshor', 'perfecing', 'estregcod']
        widgets = {
            'pernom': forms.TextInput(attrs={'class': 'form-control'}),
            'percarcoshor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'perfecing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonalActividadForm(forms.ModelForm):
    class Meta:
        model = PersonalActividad
        fields = ['actcod', 'percod']
        widgets = {
            'actcod': forms.Select(attrs={'class': 'form-control'}),
            'percod': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonalCargosPersonalForm(forms.ModelForm):
    class Meta:
        model = PersonalCargosPersonal
        fields = ['percoshorcar', 'carpercod', 'percod']
        widgets = {
            'percoshorcar': forms.NumberInput(attrs={'class': 'form-control'}),
            'carpercod': forms.Select(attrs={'class': 'form-control'}),
            'percod': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonalCargosProyectoForm(forms.ModelForm):
    class Meta:
        model = PersonalCargosProyecto
        fields = ['carprocod', 'percod']
        widgets = {
            'carprocod': forms.Select(attrs={'class': 'form-control'}),
            'percod': forms.Select(attrs={'class': 'form-control'}),
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['profecprocon', 'profecpropac', 'profecproini', 'profecproent', 'profecprocie', 'promonpro', 'promonprorea', 'promonprocos', 'promonprocosrea', 'promonprogas', 'promonprogasrea', 'promonprouti', 'promonproutirea', 'clicod', 'estregcod', 'proestprocod', 'proetaprocod', 'protipprocod']
        widgets = {
            'profecprocon': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profecpropac': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profecproini': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profecproent': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profecprocie': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'promonpro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprorea': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprocos': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprocosrea': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprogas': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprogasrea': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonprouti': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'promonproutirea': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'clicod': forms.Select(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
            'proestprocod': forms.Select(attrs={'class': 'form-control'}),
            'proetaprocod': forms.Select(attrs={'class': 'form-control'}),
            'protipprocod': forms.Select(attrs={'class': 'form-control'}),
        }

class ActividadForm(forms.ModelForm):
    complejidad = forms.ModelChoiceField(queryset=Complejidad.objects.all(), required=False, label="Complejidad")

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
    actividad = forms.ModelChoiceField(queryset=Actividad.objects.all(), required=False, label="Actividad")

    class Meta:
        model = Complejidad
        fields = ['comnom', 'comgra', 'estregcod']
    widgets = {
            'comnom': forms.TextInput(attrs={'class': 'form-control'}),
            'comgra': forms.NumberInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }
