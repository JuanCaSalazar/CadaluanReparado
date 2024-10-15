from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Importaciones para autenticación y manejo de excepciones en Django REST Framework
from rest_framework import authentication
from rest_framework import exceptions


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    """
    Gestor de modelos de usuario personalizado donde el correo electrónico es el identificador único
    para la autenticación en lugar de los nombres de usuario.
    """
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        
        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields to set on the user.

        Raises:
            ValueError: If the email is not provided.

        Returns:
            User: The created user instance.
        """
        """
        Crear y guardar un usuario con el correo electrónico y la contraseña proporcionados.
        
        Args:
            email (str): La dirección de correo electrónico del usuario.
            password (str): La contraseña para el usuario.
            **extra_fields: Campos adicionales para configurar en el usuario.

        Raises:
            ValueError: Si el correo electrónico no está proporcionado.

        Returns:
            User: La instancia de usuario creada.
        """
        # Verify that an email address is provided
        # Verificar que se proporcione una dirección de correo electrónico
        if not email:
            raise ValueError(_('The Email must be set'))
        
        # Normalize the email (e.g., convert to lowercase)
        # Normalizar el correo electrónico (por ejemplo, convertir a minúsculas)
        email = self.normalize_email(email)
        
        # Create the user instance with the email and any additional fields
        # Crear la instancia del usuario con el correo electrónico y cualquier campo adicional
        user = self.model(email=email, **extra_fields)
        
        # Set the user's password
        # Establecer la contraseña del usuario
        user.set_password(password)
        
        # Save the user to the database
        # Guardar el usuario en la base de datos
        user.save()
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        
        Superusers have additional privileges such as being staff and superuser.
        
        Args:
            email (str): The email address of the superuser.
            password (str): The password for the superuser.
            **extra_fields: Additional fields to set on the superuser.

        Raises:
            ValueError: If `is_staff` or `is_superuser` fields are not set correctly.

        Returns:
            User: The created superuser instance.
        """
        """
        Crear y guardar un superusuario con el correo electrónico y la contraseña proporcionados.
        
        Los superusuarios tienen privilegios adicionales, como ser personal y superusuario.
        
        Args:
            email (str): La dirección de correo electrónico del superusuario.
            password (str): La contraseña para el superusuario.
            **extra_fields: Campos adicionales para configurar en el superusuario.

        Raises:
            ValueError: Si los campos `is_staff` o `is_superuser` no están configurados correctamente.

        Returns:
            User: La instancia de superusuario creada.
        """
        # Set default values for superuser-specific fields
        # Establecer valores predeterminados para los campos específicos del superusuario
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('rol', "ADMIN")
        
        # Ensure that the superuser has `is_staff` and `is_superuser` set to True
        # Asegurarse de que el superusuario tenga `is_staff` e `is_superuser` establecidos en True
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        # Create the user using the `create_user` method
        # Crear el usuario utilizando el método `create_user`
        return self.create_user(email, password, **extra_fields)
