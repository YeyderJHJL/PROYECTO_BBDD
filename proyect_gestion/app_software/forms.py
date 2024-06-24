from django import forms
from .models import EstadoRegistro

class EstadoRegistroForm(forms.ModelForm):
    class Meta:
        model = EstadoRegistro
        fields = ['estregnom', 'estregestreg']
        widgets = {
            'estregnom': forms.TextInput(attrs={'class': 'form-control'}),
            'estregestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }