# Importación de módulos necesarios para el enrutamiento y la configuración de archivos estáticos
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Lista de rutas de URL del proyecto
urlpatterns = [
    # Ruta para la interfaz administrativa de Django
    path('admin/', admin.site.urls),

    # Ruta para incluir las URL definidas en el archivo urls.py de la aplicación 'reparado'
    path('', include('reparado.urls')),
]

# Configuración para servir archivos multimedia durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
