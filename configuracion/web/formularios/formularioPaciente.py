
# importar 
from django import forms

class FormularioPaciente(forms.Form):

    REGIMEN  = (
        (1,'Contributivo'),
        (2,'Subsidiado'),
    )
    GRUPOINGRESO = (
        (1,'A'),
        (2,'B'),
        (3,'C'),
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

    regimen = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select md-3"}),
        required=True,
        choices=REGIMEN        
    )

    grupoIngreso = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select md-3"}),
        required=True,
        choices=GRUPOINGRESO 
    )
    cuotaMonetaria = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "forma-control md-3"}),
        required=True,
        max_length=20
    )
    contacto = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "forma-control md-3"}),
        required=True,
        max_length=20
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "forma-control md-3"}),
        required=True,
        max_length=40
    )
