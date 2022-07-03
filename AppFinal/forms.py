from datetime import datetime
from email.policy import default
from sqlite3 import Date
from wsgiref.handlers import format_date_time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class recomendacionesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    comentarios = forms.CharField(max_length=500)
    #recomendador = forms.CharField(max_length=40, default='SOME STRING')
    #fecha = forms.DateField(default)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}




