from django import forms
from .models import Ventas
from django.contrib.auth.models import User


class Registro(forms.Form):
    '''Clase que contiene los campos del formulario de registro de clientes'''

    username = forms.CharField(required=True, min_length=5,max_length=20, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Usuario'
    }))

    email = forms.EmailField(required=True, min_length=5,max_length=40, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'ejemplo@gmail.com'
    }))

    password = forms.CharField(required=True, min_length=6,max_length=20,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña'
    }))

    password2=forms.CharField(label="Confirmar contraseña",required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirmar Contraseña',
    }))

    def clean_username(self):
        '''Funcion para vaildar el usuario'''
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya existente')#Verifica si en la base de datos existe el usuario anteriormente
        
        return username
    
    def clean_email(self):
        '''Funcion para vaildar el correo'''
        correo=self.cleaned_data.get('email')

        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('Correo ya registrado')#Verifica si en la base de datos existe el email anteriormente
        return correo
    
    def clean(self):
        #verifica que la segunda contraseña ingresada concuerde con la primera 
        cleaned_data=super().clean()

        if cleaned_data.get('password2')!= cleaned_data.get('password'):
            self.add_error('password2','Las contraseñas no coinciden')


class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'