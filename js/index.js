// Array de los productos
let productos = [];

// Se recuperam los datos de productos.json y se replican en el array
fetch("/json/productos.json")
  .then((response) => response.json())
  .then((data) => {
    productos = data;
  });

// Funciones de contadores

// Funcion que quita 1 al contador y resta al precio
function menos(idC, idP){
  // Substring al ultimo digito para poder iterar correctamente a traves de las Id's
  
  let id = idC.substring(idC.length - 1); 

  /*
  let id;
  
  if (idC.length == 8) {
    id = idC.substring(idC.length - 1); 
  }
  else {
    id = idC.substring(idC.length - 2);
  }
  */

  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el span
  let span = document.querySelector("#" + idP);
  
  // Variables
  let total;
  let precio;

  // Iteracion para recuperar el precio dependiendo la id
  for (let i = 0; i < productos.length; i++) {
    if (productos[i].id === id){
      precio = parseInt(productos[i].precio);
    }
  } 

  // Si el contador es menor a 10 se suma 1
  if (cont > 1){
    cont--;

    // Calculo del total
    total = cont * precio;

    // Variables al HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  }
  else {
    alert("El minimo de productos para añadir son 1")
  }
};

// Funcion que suma 1 y suma al precio
function mas(idC, idP){
  // Substring al ultimo digito para poder iterar correctamente a traves de las Id's
  let id = idC.substring(idC.length - 1); 

  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el span
  let span = document.querySelector("#" + idP);
  
  // Variables
  let total;
  let precio;

  // Iteracion para recuperar el precio dependiendo la id
  for (let i = 0; i < productos.length; i++) {
    if (productos[i].id === id){
      precio = parseInt(productos[i].precio);
    }
  } 

  // Si el contador es menor a 10 se suma 1
  if (cont < 10){
    cont++;

    // Calculo del total
    total = cont * precio;

    // Variables al HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  }
  else {
    alert("El maximo de productos para añadir son 10")
  }
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





