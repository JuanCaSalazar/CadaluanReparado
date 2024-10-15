// Función para cargar y mostrar un modal utilizando AJAX
function modal(ruta) {
    // Cierra cualquier modal activa
    $(".modal").modal("hide");

    // Realiza una solicitud AJAX para cargar el contenido del modal
    $.ajax({
        method: "GET",
        url: ruta,
    })
    .done(function(respuesta) {
        // Inserta la respuesta en el modal
        $("#modal").html(respuesta);

        // Inicializa y muestra el nuevo modal usando Bootstrap 5
        var myModal = new bootstrap.Modal(document.getElementById('modal'));
        myModal.show();
    })
    .fail(function() {
        // Maneja errores si la solicitud falla
        console.error("La respuesta del servidor no es válida.");
        alert("Ocurrió un error al procesar la respuesta del servidor.");
    });
}

// Función para cargar el formulario de registro en un modal
function registro(ruta) {

    // Realiza una solicitud AJAX para obtener el formulario de registro
    $.ajax({
        method: "GET",
        url: ruta,
    })
    .done(function(respuesta) {
        // Inserta el formulario en el modal correspondiente y lo muestra
        $("#registrarseModal").html(respuesta.html);
        $("#registrarseModal").modal("show");
    })
    .fail(function() {
        console.error("La respuesta del servidor no es válida.");
        alert("Ocurrió un error al procesar la respuesta del servidor.");
    });
}

// Función para cargar el formulario de registro en un modal
function recuperar(ruta) {

    // Realiza una solicitud AJAX para obtener el formulario de registro
    $.ajax({
        method: "GET",
        url: ruta,
    })
    .done(function(respuesta) {
        // Inserta el formulario en el modal correspondiente y lo muestra
        $("#registrarseModal").html(respuesta);
        $("#registrarseModal").modal("show");
        $('#iniciarSesionModal').modal('hide');
    })
    .fail(function() {
        console.error("La respuesta del servidor no es válida.");
        alert("Ocurrió un error al procesar la respuesta del servidor.");
    });
}

// Manejador para el envío de formularios mediante AJAX
$(document).off('submit', 'form.ajax-form').on('submit', 'form.ajax-form', function(e) {
    e.preventDefault();  // Evita la recarga de la página

    var form = $(this);  // Selecciona el formulario actual
    var url = form.attr('action');  // Obtiene la URL de acción del formulario
    var method = form.attr('method');  // Obtiene el método (GET/POST)
    var formData = new FormData(this);  // Captura los datos del formulario

    // Realiza la solicitud AJAX
    $.ajax({
        url: url,
        method: method,
        data: formData,
        processData: false,  // Evita el procesamiento de los datos
        contentType: false,  // Establece el tipo de contenido
        success: function(response) {
            if (response.redirect) {
                // Redirige si la respuesta contiene una URL de redirección
                window.location.href = response.redirect;
            } else {
                // Si no, actualiza el contenido del modal
                $("#registrarseModal").html(response.html);
            }
        },
        error: function() {
            alert("Ocurrió un error al enviar el formulario.");
        }
    });
});

// Función para cargar contenido en el offcanvas (carrito) usando AJAX
function offcanvas(ruta) {
    var r = $("#offcanvasRight");  // Selecciona el elemento del offcanvas

    // Realiza una solicitud AJAX para obtener el contenido del carrito
    $.ajax({
        method: "GET",
        url: ruta
    })
    .done(function(respuesta) {
        r.html(respuesta);  // Inserta el contenido en el offcanvas
        quitar_alertas();    // Llama a la función para quitar alertas
    })
    .fail(function() {
        alert("error");
    });
}

// Función para añadir un ítem al carrito mediante AJAX
function add_carrito(ruta, id) {
    var r = $("#offcanvasRight");  // Selecciona el elemento del offcanvas

    var id_solicitud = $("#id_solicitud_" + id).val();  // Obtiene el ID de la solicitud

    // Realiza la solicitud AJAX para añadir el ítem al carrito
    $.ajax({
        method: "GET",
        url: ruta,
        data: { "id_solicitud": id_solicitud }
    })
    .done(function(respuesta) {
        r.html(respuesta);  // Actualiza el contenido del carrito
        // Abre el offcanvas utilizando Bootstrap 5
        var offcanvas = $("#offcanvasRight").offcanvas('toggle');
        quitar_alertas();  // Llama a la función para quitar alertas
    })
    .fail(function() {
        alert("error");
    });
}

// Función para eliminar un ítem del carrito mediante AJAX
function del_item_carrito(ruta) {
    var r = $("#offcanvasRight");  // Selecciona el elemento del offcanvas

    // Realiza la solicitud AJAX para eliminar el ítem del carrito
    $.ajax({
        method: "GET",
        url: ruta
    })
    .done(function(respuesta) {
        r.html(respuesta);  // Actualiza el contenido del carrito
        quitar_alertas();   // Llama a la función para quitar alertas
    })
    .fail(function() {
        alert("error");
    });
}

// Función para ocultar alertas automáticamente después de 1 segundo
function quitar_alertas() {
    console.log("Quitando alerta...");
    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function() {
            $(this).remove();  // Elimina la alerta del DOM
        });
    }, 1000);
}

// Gestión del modo oscuro/claro
const toggleButton = document.getElementById('toggle-dark-mode');
const icon = toggleButton.querySelector('i');  // Selecciona el ícono en el botón
const darkModeEnabled = localStorage.getItem('dark-mode') === 'true';  // Verifica si el modo oscuro está habilitado
const htmlElement = document.documentElement;  // Selecciona el elemento <html>

// Función para actualizar el ícono del botón según el modo activo
const updateIcon = (isDarkMode) => {
    if (isDarkMode) {
        icon.classList.replace('bi-moon', 'bi-sun');  // Cambia el ícono a "sol" en modo oscuro
    } else {
        icon.classList.replace('bi-sun', 'bi-moon');  // Cambia el ícono a "luna" en modo claro
    }
};

// Función para alternar entre modo oscuro y claro
const toggleDarkMode = (isDarkMode) => {
    document.body.classList.toggle('dark-mode', isDarkMode);  // Aplica o elimina la clase 'dark-mode'
    localStorage.setItem('dark-mode', isDarkMode);  // Guarda la preferencia en localStorage

    // Cambia el tema en el atributo data-bs-theme del elemento <html>
    if (isDarkMode) {
        htmlElement.setAttribute('data-bs-theme', 'dark');
    } else {
        htmlElement.removeAttribute('data-bs-theme');
    }

    updateIcon(isDarkMode);  // Actualiza el ícono
};

// Inicializa el modo oscuro si está habilitado en localStorage
if (darkModeEnabled) {
    toggleDarkMode(true);
}

// Añade un evento al botón para cambiar entre modos al hacer clic
toggleButton.addEventListener('click', () => {
    const isDarkMode = !document.body.classList.contains('dark-mode');  // Invertir el estado actual
    toggleDarkMode(isDarkMode);
});

  // Header carousel
  $(".header-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1500,
    items: 1,
    dots: false,
    loop: true,
    nav : true,
    navText : [
        '<i class="bi bi-chevron-left"></i>',
        '<i class="bi bi-chevron-right"></i>'
    ]
});


// Service carousel
$(".service-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    center: true,
    margin: 25,
    dots: true,
    loop: true,
    nav : false,
    responsive: {
        0:{
            items:1
        },
        576:{
            items:2
        },
        768:{
            items:3
        },
        992:{
            items:2
        },
        1200:{
            items:3
        }
    }
});




// ---------Validacion fecha de nacimiento
document.getElementById('register-user-form').addEventListener('submit', function(event) {
    const fechaNacimientoInput = document.querySelector('input[name="fecha_nacimiento"]');
    const fechaNacimiento = new Date(fechaNacimientoInput.value);
    const hoy = new Date();
    
    // Verifica que la fecha de nacimiento no sea en el futuro
    if (fechaNacimiento > hoy) {
        alert("La fecha de nacimiento no puede ser en el futuro.");
        event.preventDefault();  // Detiene el envío del formulario
        return;
    }

    // Verifica que la persona tenga al menos 18 años
    const edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    const mes = hoy.getMonth() - fechaNacimiento.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
        edad--;
    }

    if (edad < 18) {
        alert("Debes ser mayor de 18 años para registrarte.");
        event.preventDefault();
    }
});