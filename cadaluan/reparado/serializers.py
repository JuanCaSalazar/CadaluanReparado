# Importación de los modelos y del módulo de serialización de DRF
from .models import *
from rest_framework import serializers


# Serializador para el modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'email', 'direccion', 'foto']  # Campos específicos


# Serializador para el modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  # Incluye todos los campos del modelo


# Serializador para el modelo Servicio
class ServicioSerializer(serializers.ModelSerializer):
    # Campo relacionado para traer el nombre de la categoría en lugar del ID
    categoria_name = serializers.StringRelatedField(many=False, source='categoria.nombre_cat')

    class Meta:
        model = Servicio
        fields = ['id', 'nombre_ser', 'desc_ser', 'precio', 'categoria', 'categoria_name', 'foto']  # Campos específicos


# Serializador para el modelo Solicitud
class SolicitudSerializer(serializers.ModelSerializer):
    # Campo relacionado para traer el nombre del servicio y el nombre del usuario
    servicio_name = serializers.StringRelatedField(many=False, source='servicio.nombre_ser')
    usuario_name = serializers.StringRelatedField(many=False, source='usuario.nombre')

    class Meta:
        model = Solicitud
        fields = ['id', 'usuario_name', 'servicio_name', 'fecha_hora', 'precio', 'tiempo_estimado', 'zona', 'usuario', 'tecnico', 'estado']


# Serializador para el modelo Factura
class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = '__all__'  # Incluye todos los campos del modelo


# Serializador para el login, usando el modelo Usuario
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'rol']  # Campos específicos para la autenticación


# Serializador para la creación de nuevos usuarios, usando el modelo Usuario
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)  # Campo obligatorio
    password = serializers.CharField(write_only=True, required=True)  # Campo obligatorio y solo escritura

    class Meta:
        model = Usuario
        fields = ['username', 'password']  # Campos necesarios para el registro

    # Método para crear un nuevo usuario con contraseña encriptada
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],  # Asigna el nombre de usuario
        )
        user.set_password(validated_data['password'])  # Encripta la contraseña
        user.save()  # Guarda el usuario en la base de datos
        return user
