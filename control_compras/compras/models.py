from django.db import models
from django.contrib.auth.models import User

class SolicitudCompra(models.Model):
    ESTADOS_CHOICES = [
        ('PENDIENTE', 'Pendiente de Revisión'),
        ('EN_PROCESO', 'En Proceso de Compra'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    ]

    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_solicitudes')
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solicitud #{self.id} de {self.solicitante.username}"


class ItemSolicitud(models.Model):
    # Cada ítem debe pertenecer obligatoriamente a una solicitud de compra
    solicitud = models.ForeignKey(SolicitudCompra, on_delete=models.CASCADE, related_name='items')
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Ítem")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción/Justificación")

    def __str__(self):
        return f"{self.nombre} (x{self.cantidad})"