from django import forms
from django.shortcuts import render, redirect
from expedientes.models import Persona, Barrio, Expediente
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from .forms import CreateNewPersona, CreateNewBarrio, CreateNewExpediente
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

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

class PersonaIndexView(TemplateView):
    model = Persona
    template_name = 'persona/persona_list.html'

class PersonaListView(BaseDatatableView):
    model = Persona
    columns = ('apellido', 'nombre', 'dni', 'edad', 'barrio')
    order_columns = ['apellido', 'nombre']

    def get_filter_method(self):
        return self.FILTER_ICONTAINS
    
    def filter_queryset(self, qs):
        filter_customer = self.request.POST.get('search[value]', None)

        if filter_customer:
            customer_parts = filter_customer.strip().split(' ')
            qs_params = Q()
            for part in customer_parts:
                qs_params &= Q(apellido__icontains=part) | Q(nombre__icontains=part)
            qs = qs.filter(qs_params)
        return qs
    
    def render_column(self, row, column):
        if column == 'acciones':
            #if self.perms.expediente.change_persona:
            if self.request.user.has_perm('expediente.change_persona'):
                btn_editar = '''<a href="%s" class="btn" style="background-color: #E3DFFD"
                    role="button" aria-pressed="true"><i class="bi-pencil"></i> Editar</a>''' % (reverse_lazy('persona_edit',args=[str(row.pk)]))
            else:
                btn_editar = '''<a class="btn" disabled style="background-color: #F3E8FF; cursor:not-allowed" role="button"
                    aria-pressed="true"><i class="bi-pencil"></i> Editar</a>'''
            #if self.perms.expediente.delete_persona:
            if self.request.user.has_perm('expediente.delete_persona'):
                btn_eliminar = '''<a href="%s" class="btn" style="background-color: #EB455F"
                    role="button" aria-pressed="true"><i class="bi-trash"></i> Eliminar</a>''' % (reverse_lazy('persona_delete',args=[str(row.pk)]))
            else:
                btn_eliminar = '''<a class="btn" disabled style="background-color: #F3E8FF; cursor:not-allowed" role="button"
                    aria-pressed="true"><i class="bi-trash"></i> Eliminar</a>'''
            return btn_editar, btn_eliminar
        return super().render_column(row, column)

class PersonaCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewPersona
    permission_required = 'expediente.create_persona'
    template_name = 'persona/persona_new.html'
    success_message = 'Se carga la persona correctamente'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(PermissionRequiredMixin, SuccessMessageMixin , UpdateView):
    model = Persona
    form_class = CreateNewPersona
    permission_required = 'expediente.view_persona'
    template_name = 'persona/persona_edit.html'
    success_message = 'Se edito correctamente la persona'
    success_url = reverse_lazy('persona_index')

class PersonaDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy('persona_index')
    permission_required = 'expediente.delete_persona'
    template_name = 'persona/persona_delete.html'
    success_message = 'Se elimino la persona correctamente'

class BarrioListView(ListView):
    model = Barrio
    template_name = 'barrio/barrio_list.html'
    ordering = ['nombre']

class BarrioCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Persona
    form_class = CreateNewBarrio
    permission_required = 'expediente.create_barrio'
    template_name = 'barrio/barrio_new.html'
    success_message = 'Se cargo el barrio correctamente'
    success_url = reverse_lazy('barrio_list')

class BarrioUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Barrio
    form_class = CreateNewBarrio
    permission_required = 'expediente.view_barrio'
    template_name = 'barrio/barrio_edit.html'
    success_message = 'Se edito correctamente el barrio'
    success_url = reverse_lazy('barrio_list')

class BarrioDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Barrio
    success_url = reverse_lazy('barrio_list')
    permission_required = 'expediente.delete_barrio'
    template_name = 'barrio/barrio_delete.html'
    success_message = 'Se elimino el barrio correctamente'

class ExpedienteListView(ListView):
    model = Expediente
    template_name = 'expediente/expediente_list.html'
    ordering = ['fecha_carga']

class ExpedienteCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Expediente
    form_class = CreateNewExpediente
    permission_required = 'expediente.create_expediente'
    template_name = 'expediente/expediente_new.html'
    success_message = 'Se cargo el expediente correctamente'
    success_url = reverse_lazy('expediente_list')

class ExpedienteUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Expediente
    form_class = CreateNewExpediente
    permission_required = 'expediente.view_expediente'
    template_name = 'expediente/expediente_edit.html'
    success_message = 'Se edito correctamente el expediente'
    success_url = reverse_lazy('expediente_list')

class ExpedienteDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Expediente
    success_url = reverse_lazy('expediente_list')
    permission_required = 'expediente.delete_expediente'
    template_name = 'expediente/expediente_delete.html'
    success_message = 'Se elimino el expediente correctamente'