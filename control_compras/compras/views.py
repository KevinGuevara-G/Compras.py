from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SolicitudCompraForm, ItemSolicitudFormSet

@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudCompraForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.solicitante = request.user
            solicitud.save() # Guardamos primero para generar el ID de la solicitud
            
            # Pasamos los datos del POST e inyectamos la solicitud recién creada
            formset = ItemSolicitudFormSet(request.POST, instance=solicitud)
            if formset.is_valid():
                formset.save()
                return redirect('crear_solicitud')
    else:
        form = SolicitudCompraForm()
        formset = ItemSolicitudFormSet()
        
    return render(request, 'crear_solicitud.html', {
        'form': form,
        'formset': formset
    })