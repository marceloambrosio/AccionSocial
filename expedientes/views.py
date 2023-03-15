from django.shortcuts import render
from expedientes.models import Persona, Barrio, Expediente
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CreateNewPersona, CreateNewBarrio, CreateNewExpediente
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index_expedientes.html')

def persona_list(request):
    persona = Persona.objects.all().order_by('apellido')
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(persona, 6)
        persona = paginator.page(page)
    except:
        raise Http404

    return render(request, 'persona/persona_list.html', {
        'entity': persona,
        'paginator': paginator
    })

class PersonaCreateViews(SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewPersona
    template_name = 'persona/persona_new.html'
    success_message = 'Se carga la persona correctamente'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateViews(SuccessMessageMixin, UpdateView):
    model = Persona
    form_class = CreateNewPersona
    template_name = 'persona/persona_edit.html'
    success_message = 'Se edito correctamente la persona'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(SuccessMessageMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy('persona_list')
    template_name = 'persona/persona_delete.html'
    success_message = 'Se elimino la persona correctamente'

def barrio_list(request):
    barrio = Barrio.objects.all().order_by('nombre')
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(barrio, 6)
        barrio = paginator.page(page)
    except:
        raise Http404

    return render(request, 'barrio/barrio_list.html', {
        'entity': barrio,
        'paginator': paginator
    })

class BarrioCreateViews(SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewBarrio
    template_name = 'barrio/barrio_new.html'
    success_message = 'Se cargo el barrio correctamente'
    success_url = reverse_lazy('barrio_list')

class BarrioUpdateViews(SuccessMessageMixin, UpdateView):
    model = Barrio
    form_class = CreateNewBarrio
    template_name = 'barrio/barrio_edit.html'
    success_message = 'Se edito correctamente el barrio'
    success_url = reverse_lazy('barrio_list')

class BarrioDeleteView(SuccessMessageMixin, DeleteView):
    model = Barrio
    success_url = reverse_lazy('barrio_list')
    template_name = 'barrio/barrio_delete.html'
    success_message = 'Se elimino el barrio correctamente'


def expediente_list(request):
    expediente = Expediente.objects.all().order_by('id')
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(expediente, 6)
        expediente = paginator.page(page)
    except:
        raise Http404

    return render(request, 'expediente/expediente_list.html', {
        'entity': expediente,
        'paginator': paginator
    })

class ExpedienteCreateViews(SuccessMessageMixin, CreateView):
    model = Expediente
    form_class = CreateNewExpediente
    template_name = 'expediente/expediente_new.html'
    success_message = 'Se cargo el expediente correctamente'
    success_url = reverse_lazy('expediente_list')

class ExpedienteUpdateViews(SuccessMessageMixin, UpdateView):
    model = Expediente
    form_class = CreateNewExpediente
    template_name = 'expediente/expediente_edit.html'
    success_message = 'Se edito correctamente el expediente'
    success_url = reverse_lazy('expediente_list')

class ExpedienteDeleteView(SuccessMessageMixin, DeleteView):
    model = Expediente
    success_url = reverse_lazy('expediente_list')
    template_name = 'expediente/expediente_delete.html'
    success_message = 'Se elimino el expediente correctamente'