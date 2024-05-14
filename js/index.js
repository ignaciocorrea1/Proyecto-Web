

// Funciones para los contadores

// Funcion para quitarle 1 al contador y restarle al precio
function menos(idCont, idPrecio) {
    // Obtencion del numero del contador
    let contador = document.querySelector("#" + idCont);
    let cont = parseInt(contador.textContent);

    // Obtencion del precio
    let prod = document.querySelector("#" + idPrecio);
    let precio = parseInt(prod.textContent);

    // Validar si el contador es mayor a 1
    if (cont > 1) {
        cont--;

        // Calculo del precio total del producto
        let total = precio * cont;
        console.log(cont, total);

        // Asignacion de valores
        contador.textContent = cont.toString();
        // prod.textContent = total.toString();
    }
    else {
        alert("El minimo es 1");
    };
};

// Funcion para agregarle 1 al contador y sumarle al precio
function mas(idCont, idPrecio) {
    // Obtencion del numero del contadord
    let contador = document.querySelector("#" + idCont);
    let cont = parseInt(contador.textContent);

    // Obtencion del precio
    let prod = document.querySelector("#" + idPrecio);
    let precio = parseInt(prod.textContent);

    // Validar si el contador es menor a 10
    if (cont < 10) {
        cont++;

        let total = precio * cont;
        console.log(cont, total);

        // Asignacion de valores
        contador.textContent = cont.toString();
        // prod.textContent = total.toString();
    }
    else {
        alert("El maximo es 10");
    };
};

// Funciones del carrito

// Formulario

function validarFormulario() {
    let nombres = document.getElementById('nombres').value;
    let rut = document.getElementById('rut').value;
    let paterno = document.getElementById('paterno').value;
    let materno = document.getElementById('materno').value;
    let correo = document.getElementById('correo').value;
    let contrasenia = document.getElementById('contrasenia').value;
    let contrasenia2 = document.getElementById('contrasenia-2').value;

    // Validación de RUT
    if (!validarRUT(rut)) {
        alert('El RUT ingresado no es válido.');
        return false;
    }

    // Validación de nombres y apellidos
    if (!validarTexto(nombres) || !validarTexto(paterno) || !validarTexto(materno)) {
        alert('Los nombres y apellidos solo deben contener letras.');
        return false;
    }

    // Validar que el correo sea de Gmail o Outlook
    let correoRegex = /^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com)$/i;
    if (!correoRegex.test(correo)) {
        alert('El correo debe ser de Gmail o Outlook.');
        return false;
    }

    // Validación de contraseña
    if (!validarContrasenia(contrasenia)) {
        alert('La contraseña debe tener al menos 8 caracteres, incluyendo números y letras.');
        return false;
    }

    // Verificar que las contraseñas coincidan
    if (contrasenia !== contrasenia2) {
        alert('Las contraseñas no coinciden.');
        return false;
    }

    return true; // Todas las validaciones son correctas
}

function validarRUT(rut) {
    let re = /^\d{7,8}-[\dkK]$/;
    return re.test(rut);
}

function validarTexto(texto) {
    let re = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;
    return re.test(texto);
}

function validarContrasenia(contrasenia) {
    let re = /^(?=.*\d)(?=.*[a-zA-Z]).{8,}$/;
    return re.test(contrasenia);
}






