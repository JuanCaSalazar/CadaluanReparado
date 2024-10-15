from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.html import mark_safe


# Register your models here.

class UsuarioAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios
    list_display = ['username', 'nombre', 'apellido', 'email', 'is_staff']

    # Campos por los que se puede buscar
    search_fields = ['nombre', 'apellido', 'email', 'username']

    # Campos que se mostrarán en el formulario de edición de usuarios
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal',
         {'fields': ('nombre', 'apellido', 'email', 'direccion', 'fecha_nacimiento', 'telefono', 'foto')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Otros', {'fields': ('token', 'rol', 'categorias')}),
    )

    # Campos que se mostrarán en el formulario de creación de nuevos usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'direccion', 'fecha_nacimiento',
                'telefono', 'foto', 'token', 'rol', 'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions'),
        }),
    )

    # Campos que se mostrarán en la lista de usuarios
    list_display = ('username', 'nombre', 'apellido', 'email', 'is_staff')

    # Campos por los que se puede buscar
    search_fields = ('username', 'nombre', 'apellido', 'email')

    # Ordenar por defecto
    ordering = ('username',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre_cat', 'desc']
    search_fields = ['nombre_cat']  # Para realizar busquedas


class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_ser', 'desc_ser', 'precio', 'categoria', 'ver_foto']
    search_fields = ["nombre", "categorias_nombre_cat", "categorias_desc"]
    list_filter = ["categoria"]

    # list_editable = ["nombre", "categorias"]

    def ver_foto(self, obj):
        return mark_safe(f"<img src='{obj.foto.url}' width='30%' />")

    def id_cat(self, obj):
        return obj.categorias.id


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['id', 'servicio', 'categoria', 'fecha_hora', 'precio', 'usuario']
    search_fields = ['id', 'usuario']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Factura)
admin.site.register(Compra)

