from django import forms
from .models import SolicitudCompra

class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        # Solo mostramos los campos que el empleado debe llenar
        fields = ['item_codigo', 'cantidad', 'descripcion']
        widgets = {
            'item_codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. LPT-001'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Justifique su requerimiento...'}),
        }