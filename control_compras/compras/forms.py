from django import forms
from django.forms import inlineformset_factory
from .models import SolicitudCompra, ItemSolicitud

class SolicitudCompraForm(forms.ModelForm):
    class Meta:
        model = SolicitudCompra
        fields = [] # La solicitud principal se genera sin campos directos del usuario por ahora

# Creamos el set de formularios inline para los ítems vinculados a la solicitud
ItemSolicitudFormSet = inlineformset_factory(
    SolicitudCompra,
    ItemSolicitud,
    fields=['codigo', 'cantidad', 'descripcion'],
    extra=1, # Define cuántos renglones vacíos se le mostrarán al usuario por defecto
    widgets={
        'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. P001'}),
        'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Opcional...'}),
    }
)