document.addEventListener('DOMContentLoaded', function() {
   
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const nombre = document.getElementById('nombre').value;
            const email = document.getElementById('email').value;
            const mensaje = document.getElementById('mensaje').value;
            
            if (!nombre.trim()) {
                alert('Por favor, ingresa tu nombre completo.');
                return;
            }
            
            if (!email.trim()) {
                alert('Por favor, ingresa tu correo electrónico.');
                return;
            }
            
            if (!mensaje.trim()) {
                alert('Por favor, escribe el motivo de tu mensaje.');
                return;
            }
            
            alert('Mensaje enviado correctamente, gracias por escribirnos');
            contactForm.reset();
        });
    }
});