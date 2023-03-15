from django import forms
from .models import Persona, Barrio, Expediente
from django.forms import ModelForm, TextInput, NumberInput, Select, DateInput


class CreateNewPersona(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'dni', 'barrio', 'domicilio', 'telefono']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha_nacimiento': DateInput(
                attrs={
                    'class': 'form-control',
                    'type' : 'date',
                }
            ),
            'dni': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'barrio': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'telefono': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CreateNewBarrio(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre','descripcion']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class CreateNewExpediente(ModelForm):
    class Meta:
        model = Expediente
        fields = ['fecha_carga', 'fecha_intervencion',
                  'numero_expediente','numero_interno', 'persona']
        widgets = {
            'fecha_carga': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'fecha_intervencion': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'numero_expediente': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'numero_interno': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'persona': Select(
                attrs={
                    'class': 'form-control'
                }
            ),            
        }