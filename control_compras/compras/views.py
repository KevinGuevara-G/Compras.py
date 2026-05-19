from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SolicitudCompraForm

@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudCompraForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.solicitante = request.user  # Asignamos automáticamente al usuario actual
            solicitud.save()
            return redirect('crear_solicitud')  # Por ahora redirige aquí mismo o a una lista de éxitos
    else:
        form = SolicitudCompraForm()
    
    return render(request, 'compras/crear_solicitud.html', {'form': form})