//CREA LA FUNCION DE REGISTRO

document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('formularioRegistro');
    const mensajeError = document.getElementById('mensajeError');
    const salidaDatos = document.getElementById('salidaDatos');


    //escuchar el evento
});

document.getElementById("registroForm").addEventListener("submit", function (event) {
    // El navegador ya previene el envío si falta algún required
    if (this.checkValidity()) {
        event.preventDefault(); // Previene el envío real
        alert("¡Sus datos han sido enviados con éxito!");
        // Aquí podrías también limpiar el formulario o redirigir, si lo deseas
        this.reset();
    } else {
        // Si no es válido, permite que el navegador muestre sus mensajes
    }
});
