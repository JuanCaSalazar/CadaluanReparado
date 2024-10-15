/* split- landing page */

const left = document.querySelector('.left')
const right = document.querySelector('.right')
const container = document.querySelector('.container2')

left.addEventListener('mouseenter', () => container.classList.add('hover-left'))
left.addEventListener('mouseleave', () => container.classList.remove('hover-left'))

right.addEventListener('mouseenter', () => container.classList.add('hover-right'))
right.addEventListener('mouseleave', () => container.classList.remove('hover-right'))


/* estilos js preguntas */

document.addEventListener('DOMContentLoaded', () => {
    const toggles = document.querySelectorAll('.faq-toggle');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const faq = toggle.parentNode;
            faq.classList.toggle('active');

            // Alternar visibilidad del texto
            const text = faq.querySelector('.faq-text');
            if (faq.classList.contains('active')) {
                text.style.display = 'block'; // Mostrar
            } else {
                text.style.display = 'none'; // Ocultar
            }
        });
    });
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

   // Facts counter
   $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000
});

