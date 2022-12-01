
# importar 
from django import forms

class FormularioMedico(forms.Form):

    ESPECIALIDADES = (
        (1,'Cardiología'),
        (2,'Medicina Interna'),
        (3,'Medicina General'),
        (4,'Ortopedia'),
        (5,'Pedriatria'),
    )
    JORNADAS = (
        (1,'6:00 am - 2:00 pm'),
        (2,'2:00 pm - 10:00 pm'),
        (3,'10:00 pm - 6:00 am'),
    )
    SEDES = (
        (1,'Almacentro'),
        (2,'Punto clave'),
        (3,'Molinos'),
    )

# Formulario
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control md-3"}),
        required=True,
        max_length=15
    )

    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control md-3"}),
        required=True,
        max_length=35
    )

    cedula = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control md-3"}),
        required=True,
        max_length=10
    )

    tarjetaProfesional = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control md-3"}),
        required=True,
        max_length=20
    )
    especialidad = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select md-3"}),
        required=True,
        choices=ESPECIALIDADES        
    )

    jornada = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select md-3"}),
        required=True,
        choices=JORNADAS 
    )
    contacto = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "forma-control md-3"}),
        required=True,
        max_length=20
    )
    sede = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select md-3"}),
        required=True,
        choices=SEDES 
    )