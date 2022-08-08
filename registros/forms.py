
from django import forms
from .models import Alumnos, ComentarioContacto
from tkinter import Widget
from django import forms
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ('usuario', 'mensaje')

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('matricula','nombre', 'carrera', 'turno')

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label>%(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo', 'descripcion', 'archivo')
        Widgets = {
            'archivo': CustomClearableFileInput
        }
