from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from datetime import date


class RegistroForm(UserCreationForm):
    # Definir el campo 'username' de manera explícita
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Alias de usuario'
        }),
        label='Nombre de usuario'
    )

    # Campo 'email' personalizado
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )

    # Campo 'nombre'
    nombre = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        }),
        label='Nombre'
    )

    # Campo 'apellido'
    apellido = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        }),
        label='Apellido'
    )

    # Campo 'password1' personalizado
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }),
        label='Contraseña'
    )

    # Campo 'password2' personalizado
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        }),
        label='Confirmar Contraseña'
    )

    # Campo 'fecha_nacimiento'
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Fecha de Nacimiento',
            'type': 'date',
              # Esto permite que el navegador muestre un selector de fecha
        }),
        label='Fecha de Nacimiento'
        
    )
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        hoy = date.today()

        if not fecha_nacimiento:
            raise ValidationError("Este campo es obligatorio.")

        # Verifica que la fecha de nacimiento no sea en el futuro
        if fecha_nacimiento > hoy:
            raise ValidationError("La fecha de nacimiento no puede ser en el futuro.")

        # Verifica que la persona sea mayor de 18 años
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if edad < 18:
            raise ValidationError("Debes ser mayor de 18 años para registrarte.")

        return fecha_nacimiento

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'apellido', 'fecha_nacimiento', 'foto']

    # Validación personalizada para el correo electrónico
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email

    # Validación personalizada para el nombre de usuario
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está registrado.")
        return username
    




class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'nombre',
            'apellido',
            'email',
            'fecha_nacimiento',
            'direccion',
            'telefono',
            'foto',
            'rol',  # Solo si es necesario para el administrador
        ]

    def clean(self):
        cleaned_data = super().clean()
        # Añade tus validaciones personalizadas aquí
        return cleaned_data

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'email', 'fecha_nacimiento', 'direccion', 'telefono', 'foto', 'rol', 'categorias']
    
    