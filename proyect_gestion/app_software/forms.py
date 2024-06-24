from django import forms
from .models import EstadoRegistro

class EstadoRegistroForm(forms.ModelForm):
    class Meta:
        model = EstadoRegistro
        fields = ['estregnom', 'estregestreg']