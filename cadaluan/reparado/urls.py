# Importación de módulos necesarios para el enrutamiento y la documentación
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Configuración del enrutador de DRF para las vistas basadas en conjuntos de vistas
router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'servicio', views.ServicioViewSet)
router.register(r'solicitud', views.SolicitudViewSet)
router.register(r'factura', views.FacturaViewSet)

# Lista de rutas de URL del proyecto
urlpatterns = [
    # URL base para la API, incluye las rutas generadas por el enrutador
    path("api/1.0/", include(router.urls)),

    # Ruta para la documentación de la API (usando DRF)
   #path('api/1.0/docs/', include_docs_urls(title='Reparado API')),

    # Ruta para filtrar servicios por categoría
    path('api/1.0/servicios_por_cat/<int:categorias>/', views.ServicioFiltroCategoria.as_view()),

    # Ruta para la autenticación de tokens para aplicaciones móviles
    path('api/1.0/token-auth/', views.CustomAuthToken.as_view()),

    # Ruta para la autenticación de sesión web
    path('api/1.0/auth/', include("rest_framework.urls")),

    # Ruta para el registro de nuevos usuarios a través de la API
    path('api/1.0/register/', views.RegisterView.as_view(), name='register'),

     # panel solo para el admin
     path("admin_panel/", views.admin_panel, name="admin_panel"),

    # Rutas para el sistema de inicio de sesión y gestión de usuarios en la interfaz web
    path('', views.index, name='index'),  # Página principal
    path("calendario/", views.calendario, name="calendario"),  # Vista de calendario
    path("login/", views.login, name="login"),  # Vista de inicio de sesión
    path("inicio/", views.inicio, name="inicio"),  # Página de inicio
    path("logout/", views.logout, name="logout"),  # Vista de cierre de sesión
    path("registro/", views.registro, name="registro"),  # Vista de registro
    path("cambiar_clave/", views.cambiar_clave, name="cambiar_clave"),  # Cambio de contraseña
    path("recuperar_clave/", views.recuperar_clave, name="recuperar_clave"),  # Recuperación de contraseña
    path("verificar_token_form/<str:email>/", views.verificar_token_form, name="verificar_token_form"),  # Verificación de token para formulario
    path("olvide_mi_clave/<str:email>/", views.olvide_mi_clave, name="olvide_mi_clave"),  # Recuperación de clave por email

    # Rutas para la gestión de categorías
    path("categorias/", views.categorias, name="categorias"),  # Listar categorías
    path("categorias_crear/", views.categorias_crear, name="categorias_crear"),  # Crear nueva categoría
    path("categorias_editar/<int:id_categoria>/", views.categorias_editar, name="categorias_editar"),  # Editar categoría existente
    path("categorias_eliminar/<int:id_categoria>/", views.categorias_eliminar, name="categorias_eliminar"),  # Eliminar categoría

    # Rutas para la gestión de servicios
    path("servicios/", views.servicios, name="servicios"),  # Listar servicios
    path("servicios_crear/", views.servicios_crear, name="servicios_crear"),  # Crear nuevo servicio
    path("servicios_editar/<int:id_servicio>/", views.servicios_editar, name="servicios_editar"),  # Editar servicio existente
    path("servicios_eliminar/<int:id_servicio>/", views.servicios_eliminar, name="servicios_eliminar"),  # Eliminar servicio

    # Rutas para la gestión de solicitudes
    path("solicitudes/", views.solicitudes, name="solicitudes"),  # Listar solicitudes
    path("solicitud_servicio/<int:id_servicio>/", views.solicitud_servicio, name="solicitud_servicio"),  # Crear solicitud de servicio
    path("solicitud_editar/<int:id_solicitud>/", views.solicitud_editar, name="solicitud_editar"),  # Editar solicitud existente
    path("solicitud_eliminar/<int:id_solicitud>/", views.solicitud_eliminar, name="solicitud_eliminar"),  # Eliminar solicitud

    # Rutas para la gestión de usuarios
    path("usuarios/", views.usuarios, name="usuarios"),  # Listar usuarios
    path("usuarios_crear/", views.usuarios_crear, name="usuarios_crear"),  # Crear nuevo usuario
    path("usuarios_visualizar/<int:id_usuario>/", views.usuarios_visualizar, name="usuarios_visualizar"),  # Visualizar perfil de usuario
    path("visualizar_perfil/<int:id_usuario>/", views.visualizar_perfil, name="visualizar_perfil"),  # Ver perfil del usuario
    path("usuarios_editar/<int:id_usuario>/", views.usuarios_editar, name="usuarios_editar"),  # Editar usuario existente
    path("usuarios_eliminar/<int:id_usuario>/", views.usuarios_eliminar, name="usuarios_eliminar"),  # Eliminar usuario

    # Rutas para el carrito de compras
    path("carrito_add/<int:id>/", views.carrito_add, name="carrito_add"),  # Añadir item al carrito
    path("ver_carrito/", views.ver_carrito, name="ver_carrito"),  # Ver contenido del carrito
    path("eliminar_item_carrito/<int:id_solicitud>/", views.eliminar_item_carrito, name="eliminar_item_carrito"),  # Eliminar item del carrito
    path("vaciar_carrito/", views.vaciar_carrito, name="vaciar_carrito"),  # Vaciar el carrito
    path("guardar_compra/", views.guardar_compra, name="guardar_compra"),  # Confirmar compra
    path("generar_factura/<int:compra_id>/", views.generar_factura, name="generar_factura"),  # Ver detalles de una compra específica
    path('procesar_pago/<int:compra_id>/', views.procesar_pago, name='procesar_pago'),
    path("detalle_compras/", views.detalle_compras, name="detalle_compras"),  # Listar detalles de todas las compras

    # Ruta para el envío de correos
    path("enviar_correo/", views.enviar_correo, name="enviar_correo"),  # Enviar un correo electrónico

     # footer
    path("contactanos/", views.contactanos, name="contactanos"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("nuestros_servicios/", views.nuestros_servicios, name="nuestros_servicios"),
    path("politica_privacidad/", views.politica_privacidad, name="politica_privacidad"),
    path("siguenos/", views.siguenos, name="siguenos"),
     path("pregunta/", views.pregunta, name="pregunta"),

      # tecnico
    path("tecnico/", views.tecnico, name="tecnico"),


    # descargar factura en pdf
     path('factura/<int:factura_id>/pdf/', views.generar_factura_pdf, name='generar_factura_pdf'),

    
]
