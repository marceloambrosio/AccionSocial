from django.contrib import admin
from .models import Persona, Barrio, Expediente

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ('apellido','nombre'),
    ordering = ['apellido','nombre']

class BarrioAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']

class ExpedienteAdmin(admin.ModelAdmin):
    ordering = ['numero_interno']


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Expediente, ExpedienteAdmin)