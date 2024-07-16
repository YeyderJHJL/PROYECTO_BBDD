from django import forms
from .models import *
# GENERALES ####################################################################################

class EstadoRegistroForm(forms.ModelForm):
    class Meta:
        model = EstadoRegistro
        fields = ['estregnom', 'estregestreg']
        widgets = {
            'estregnom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

# PROYECTO #####################################################################################
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

class CargosProyectoForm(forms.ModelForm):
    class Meta:
        model = CargosProyecto
        fields = ['carpronom', 'prosec', 'estregcod']
        widgets = {
            'carpronom': forms.TextInput(attrs={'class': 'form-control'}),
            'prosec': forms.Select(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
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

# ETAPAS #######################################################################################

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

# ACTIVIDADES ##################################################################################

class IncidenciasForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ['incfecini', 'incnom', 'incfecfin', 'incdes']
        widgets = {
            'incfecini': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'incfecfin': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['incfecini'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['incfecfin'].input_formats = ['%Y-%m-%dT%H:%M']

class ComplejidadForm(forms.ModelForm):
    class Meta:
        model = Complejidad
        fields = ['comnom', 'comgra', 'estregcod']

class ActividadForm(forms.ModelForm):
    complejidad = forms.ModelChoiceField(queryset=Complejidad.objects.all(), required=False, label="Complejidad")
    incidencias = forms.ModelMultipleChoiceField(queryset=Incidencias.objects.none(), required=False, label="Incidencias")

    class Meta:
        model = Actividad
        fields = ['actnom', 'actfecini', 'actfecfin', 'acttip', 'acthortradia', 'estregcod', 'complejidad', 'incidencias']
        widgets = {
            'actfecini': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'actfecfin': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'acthortradia': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['actfecini'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['actfecfin'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['acthortradia'].input_formats = ['%H:%M']
        if self.instance.pk:
            self.fields['incidencias'].queryset = Incidencias.objects.filter(actcod=self.instance.pk)

# PERSONAL ######################################################################################

class CargosPersonalForm(forms.ModelForm):
    class Meta:
        model = CargosPersonal
        fields = ['carpernom', 'estregcod']
        widgets = {
            'carpernom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['percod', 'pernom', 'percarcoshor', 'perfecing', 'estregcod'] 
        widgets = {
            'percod': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),  
            'pernom': forms.TextInput(attrs={'class': 'form-control'}),
            'percarcoshor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'perfecing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_perdni(self):
        percod = self.cleaned_data['percod']
        if Personal.objects.filter(percod=percod).exists():
            raise forms.ValidationError(" Error: Este DNI ya está registrado.")
        return percod

# CLIENTE ####################################################################################

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
            raise forms.ValidationError(" Error: Este DNI ya está registrado.")
        return clidni
    def clean_clidni(self):
        clidni = self.cleaned_data['clidni']
        if self.instance.pk is None:  # Creando un nuevo cliente
            # Validar que el DNI no esté duplicado al crear
            if Cliente.objects.filter(clidni=clidni).exists():
                raise forms.ValidationError("Este DNI ya está registrado. Ingrese un DNI válido.")
        return clidni

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['percod', 'pernom', 'percarcoshor', 'perfecing', 'estregcod'] 
        widgets = {
            'percod': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),  
            'pernom': forms.TextInput(attrs={'class': 'form-control'}),
            'percarcoshor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'perfecing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estregcod': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_percod(self):
        percod = self.cleaned_data['percod']
        if self.instance.pk:  # Si es una instancia existente (edición), no validar el DNI
            return percod
        # Validar que no exista otro registro con el mismo DNI
        if Personal.objects.filter(percod=percod).exists():
            raise forms.ValidationError("Ya existe un personal con este DNI.")
        return percod

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
