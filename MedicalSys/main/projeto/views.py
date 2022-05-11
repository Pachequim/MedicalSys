from django.shortcuts import render
from .models import Medico
from .forms import medicoForm

# Views de médico e paciente

def List_medico(request):
    medico = Medico.object.all()
    return render(request, 'medicoForm', {'medico':medico}),

def Create_medico(request):
    form = medicoForm(request.Post or None)

    if form.is_valid():
        form.save()
        return redirect('List_medico')
     return render(request, 'medico-form.html', {'form': form})

def Update_medico():
    medico = Medico.object.get(id=id)
    form = medicoForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()