from django.contrib import admin
from .models import SolicitudCompra

@admin.register(SolicitudCompra)
class SolicitudCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_codigo', 'solicitante', 'cantidad', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('item_codigo', 'solicitante__username')