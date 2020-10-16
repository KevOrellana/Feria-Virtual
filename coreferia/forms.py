from django import forms
from django.forms import ModelForm
from .models import Producto,ClExterno, Productor, ClInterno,Consultor
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nom_prod','fecha_prod','foto_prod','precio','cantidad','productor_rut']



class ClExternoForm(forms.ModelForm):
    class Meta:
        
        model = ClExterno
        fields = ('rut',
                  'nom_comp',
                  'fecha_nac',
                  'pais',
                  'telefono',
                  'direccion',
                  'correo',
                  'auth_user_username')

        labels = {'rut': 'Rut',
                  'nom_comp': 'Nombre completo',
                  'fecha_nac':'Fecha de nacimiento',
                  'pais':'Pais',
                  'telefono':'Telefono',
                  'direccion':'Direccion',
                  'correo':'Correo',
                  'auth_user_username':'Nombre de usuario (Confirmación)'}


class CustomUserForm(UserCreationForm):
    pass

class ClInternoForm(forms.ModelForm):

    class Meta:
        model = ClInterno
        fields = (
            'rut',
            'nom_comp',
            'fecha_nac',
            'direccion',
            'telefono',
            'correo',
            'auth_user_username'
        )
        labels = {'rut': 'Rut',
                  'nom_comp': 'Nombre completo',
                  'fecha_nac':'Fecha de nacimiento',
                  'direccion':'Direccion',
                  'telefono':'Telefono',
                  'correo':'Correo',
                  'auth_user_username':'Nombre de usuario (Confirmación)'}


class ProductorForm(forms.ModelForm):

    class Meta:
        model = Productor
        fields = (
            'rut',
            'nombre_completo',
            'fecha_nac',
            'correo',
            'telefono',
            'direccion',
            'auth_user_username'
        )
        labels = {'rut': 'Rut',
                  'nombre_completo': 'Nombre completo',
                  'fecha_nac':'Fecha de nacimiento',
                  'correo':'Correo',
                  'telefono':'Telefono',
                  'direccion':'Direccion',
                  'auth_user_username':'Nombre de usuario (Confirmación)'}



class ConsultorForm(forms.ModelForm):

    class Meta:
        model = Consultor
        fields = (
            'rut',
            'nombre_comp',
            'correo',
            'direccion',
            'telefono',            
            'auth_user_username'
        )
        labels = {'rut': 'Rut',
                  'nombre_comp': 'Nombre completo',
                  'correo':'Correo',
                  'direccion':'Direccion',                  
                  'telefono':'Telefono',                  
                  'auth_user_username':'Nombre de usuario (Confirmación)'}
