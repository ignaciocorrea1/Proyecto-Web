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
  // Obtencion la Id para iterar
  let id;
  
  if (idC.length == 16) {
    id = idC.substring(15, 16); 
  }
  else if (idC.length == 17) {
    id = idC.substring(15, 17);
  }
  
  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el span
  let span = document.querySelector("#" + idP);
  
  // Variables
  let total;
  let precio;

  // Iteracion para recuperar el precio dependiendo la id
  productos.forEach(tmp => {
    if (tmp.id === id) {
      precio = parseInt(tmp.precio);
    }
  });

  // Si el contador es menor a 10 se suma 1
  if (cont > 1){
    cont--;

    // Calculo del total
    total = cont * precio;

    // Variables al HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  }
};

// Funcion que suma 1 y suma al precio
function mas(idC, idP){
  // Obtencion la Id para iterar
  let id;
  
  if (idC.length == 16) {
    id = idC.substring(15, 16); 
  }
  else if (idC.length == 17) {
    id = idC.substring(15, 17);
  }
  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el span
  let span = document.querySelector("#" + idP);
  
  // Variables
  let total;
  let precio;

  // Iteracion para recuperar el precio dependiendo la id
  productos.forEach(tmp => {
    if (tmp.id === id) {
      precio = parseInt(tmp.precio);
    }
  });

  // Si el contador es menor a 10 se suma 1
  if (cont < 100){
    cont++;

    // Calculo del total
    total = cont * precio;

    // Variables al HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  }
};

// Funciones del carrito




