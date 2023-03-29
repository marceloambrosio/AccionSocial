from django.shortcuts import render, redirect
from expedientes.models import Persona, Barrio, Expediente
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import CreateNewPersona, CreateNewBarrio, CreateNewExpediente
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('/expedientes')


def index(request):
    return render(request, 'index_expedientes.html')

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    paginate_by = 6
    ordering = ['apellido']

class PersonaCreateView(SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewPersona
    template_name = 'persona/persona_new.html'
    success_message = 'Se carga la persona correctamente'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(SuccessMessageMixin, UpdateView):
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

class BarrioListView(ListView):
    model = Barrio
    template_name = 'barrio/barrio_list.html'
    ordering = ['nombre']

class BarrioCreateView(SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewBarrio
    template_name = 'barrio/barrio_new.html'
    success_message = 'Se cargo el barrio correctamente'
    success_url = reverse_lazy('barrio_list')

class BarrioUpdateView(SuccessMessageMixin, UpdateView):
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

class ExpedienteListView(ListView):
    model = Expediente
    template_name = 'expediente/expediente_list.html'
    ordering = ['fecha_carga']

class ExpedienteCreateView(SuccessMessageMixin, CreateView):
    model = Expediente
    form_class = CreateNewExpediente
    template_name = 'expediente/expediente_new.html'
    success_message = 'Se cargo el expediente correctamente'
    success_url = reverse_lazy('expediente_list')

class ExpedienteUpdateView(SuccessMessageMixin, UpdateView):
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