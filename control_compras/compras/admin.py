from django.contrib import admin
from .models import SolicitudCompra, ItemSolicitud

# Esto permite editar los ítems directamente desde la vista de la Solicitud
class ItemSolicitudInline(admin.TabularInline):
    model = ItemSolicitud
    extra = 0 # No agregar filas extras vacías en el admin a menos que se pida

@admin.register(SolicitudCompra)
class SolicitudCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitante', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('solicitante__username',)
    inlines = [ItemSolicitudInline]