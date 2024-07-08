// Array de los productos
let productos = [];

// Se recuperan los datos de productos.json y se replican en el array
fetch("/static/json/productos.json")
  .then((response) => response.json())
  .then((data) => {
    productos = data;
  });

// Funciones de contadores

// Funcion que quita 1 al contador y resta al precio
function menos(idC, idP){
  // Obtencion de la Id para obtner el precio base del producto
  let id = idC.substring(11); 
  let total;
  let precio;
  
  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el precio
  let span = document.querySelector("#" + idP);
  
  // Iteracion para recuperar el precio del producto dependiendo la id
  productos.forEach(tmp => {
    if (tmp.id === id) {
      precio = parseInt(tmp.precio);
    };
  });

  // Si el contador es mayor a 1 se resta 1
  if (cont > 1){
    cont--;

    // Calculo del precio total por el producto 
    total = cont * precio;

    // Se actualiza el contador y precio en el HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  };
};

// Funcion que suma 1 al contador y suma al precio
function mas(idC, idP){
  // Obtencion de la Id para obtner el precio base del producto
  let id = idC.substring(11); 
  let total;
  let precio;

  // Se recupera el contador
  let contador = document.querySelector("#" + idC);
  let cont = parseInt(contador.textContent);

  // Se recupera el precio
  let span = document.querySelector("#" + idP);
   
  // Iteracion para recuperar el precio del producto dependiendo la id
  productos.forEach(tmp => {
    if (tmp.id === id) {
      precio = parseInt(tmp.precio);
    };
  });

  // Si el contador es menor a 100 se suma 1
  if (cont < 100){
    cont++;

    // Calculo del precio total por el producto 
    total = cont * precio;

    // Se actualiza el contador y precio en el HTML
    contador.textContent = cont.toString();
    span.innerHTML = '$' + total;
  };
};

// Funcion para reestablecer el precio del producto y el contador sobre el modal al cerrarlo por la X
function reestablecer(idM) {
  // Substring a la id del modal para recuperar el precio y contador asociados a ese modal
  let id = idM.substring(6);

  // La iteracion busca en el json el precio asociado a la id y lo obtenido se setea en el HTML
  productos.forEach((tmp) => {
    if (tmp.id === id) {
      document.querySelector("#h-precio-" + id).textContent = "$" + tmp.precio;
      document.querySelector("#h-contador-" + id).textContent = 1;
    };
  });
};

// Control del cierre del modal haciendo clic fuera de el
document.addEventListener('DOMContentLoaded', () => {
  // Obtengo todos los modales
  let modales = document.querySelectorAll('.modal');

  // Itero sobre todos los modales
  modales.forEach(modal => {
    // Agrego el evento que lo cierra apretando fuera
    modal.addEventListener('hidden.bs.modal', function() {
      // Le paso a la funcion de reestablecer la id del modal
      reestablecer(modal.id);
    })
  });
});

// Funciones del carrito

// Funcion que añade el contador del carrito a localStorage
function add_Update_Contador(){
  // Se obtiene el contador desde el localStorage. En caso de no existir devolverá 0
  let contLocal = JSON.parse(localStorage.getItem("carrito_contador")) || 0;

  let contAct = contLocal + 1; 
  // Se actualiza el localStorage
  localStorage.setItem("carrito_contador", JSON.stringify(contAct));
}

// Funcion que añade el contador del carrito a localStorage
function del_Contador(){
  // Se obtiene el contador desde el localStorage. En caso de no existir devolverá 0
  let contLocal = JSON.parse(localStorage.getItem("carrito_contador")) || 0;

  let contAct = contLocal - 1; 
  // Se actualiza el localStorage
  localStorage.setItem("carrito_contador", JSON.stringify(contAct));
}

// Funcion que retorna el contador de productos del carrito
function returnContador(){
  return contador = JSON.parse(localStorage.getItem("carrito_contador")) || 0;
}

// Funcion que carga el contador
function loadContador(){
  let contador = returnContador();
  document.getElementById("shopping-contador").textContent = contador;
}

// Se actualiza en el HTML el contador
document.addEventListener('DOMContentLoaded', () => {
  loadContador();
});

// Funcion que añade los productos del carrito a localStorage
function add_Update_Carrito(producto){
  // Se obtiene el carrito desde localStorage. En caso de no existir se un array vacio
  let carrito = JSON.parse(localStorage.getItem("carrito_local")) || [];

  // Se verifica que el producto en el carrito no exista
  let proExiste = carrito.find(tmp => tmp.id === producto.id);

  // En caso de existir se acutliza la cantidad y el precio
  if (proExiste){
    proExiste.precio += producto.precio;
    proExiste.cantidad += producto.cantidad;
  } else {
    // Se actualiza el contador
    add_Update_Contador();
    loadContador();
    carrito.push(producto);
  }

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
};

// Funcion que retorna el carrito
function returnCarrito(){
  return JSON.parse(localStorage.getItem("carrito_local")) || [];
}

// Funcion para agregar productos desde el menu al carrito
function agregar(idAdd) {
  let id;
  let pre;
  let pre2;
  let con; 
  let nom;
  let img;

  // Saber si el producto que se quiere agregar viene desde el index o el menu
  if (String(idAdd).includes("i-")) {
    id = idAdd.substring(6);
    // Obtencion del precio y la cantidad del producto elegido
    pre = document.querySelector("#i-precio-" + id).textContent;
    pre2 = parseInt(pre.substring(1));
    con = 1;
  } else {
      id = idAdd.substring(4);
      // Obtencion del precio y la cantidad del producto elegido
      pre = document.querySelector("#h-precio-" + id).textContent;
      pre2 = parseInt(pre.substring(1));
      con = parseInt(document.querySelector("#h-contador-" + id).textContent);
  };

  // Iteracion para obtener los datos faltantes del producto a traves del json
  productos.forEach((tmp) => {
    if (tmp.id === id) {
      nom = tmp.nombre;
      img = tmp.imagen;
    }
  });

  // Se crea el producto
  let producto = {
    id: id,
    nombre: nom,
    imagen: img,
    precio: pre2,
    cantidad: con
  };

  // Se añade al carrito
  add_Update_Carrito(producto);
};

// Funcion que despliega los productos agregados al carrito
function desplegar() {
  // Se trae el carrito
  let carrito = returnCarrito();

  // Se limpia el carrito
  let contenedor = document.getElementById("d-products");
  contenedor.innerHTML = "";

  // Se recorre el carrrito para desplegar en el HTML todo lo que este ahi
  carrito.forEach(tmp => {
    // Se crea una variable para se usan template literals para incrustar 
    // los datos al HTML de una manera mas eficiente,tambien se evitan conflictos con 
    // las funciones del onclick. Las plantillas permiten insertar variables y expresiones 
    // dentro de las llaves ${} se usan `` para abrirlas y cerrarlas
    let product = `<div class="product-container">
                    <div class="product-desc">
                      <h2>${tmp.nombre}</h2>
                      <img src="${tmp.imagen}" alt="Cargando imagen...">
                      <button onclick="eliminar('d-eliminar-${tmp.id}')" class="product-remove" id="d-eliminar-${tmp.id}">Eliminar</button>
                    </div>
                    <div class="product-desc-2">
                      <div class="product-price">
                        <span class="precio">Precio:</span>
                        <span class="precio-2" id="d-precio-${tmp.id}">$${tmp.precio}</span>
                      </div>
                      <div class="product-add">
                        <button onclick="menos('d-contador-${tmp.id}', 'd-precio-${tmp.id}'), reducirTotal('${tmp.id}')" class="product-menos">-</button>
                        <span class='product-contador' id='d-contador-${tmp.id}'>${tmp.cantidad}</span>
                        <button onclick="mas('d-contador-${tmp.id}', 'd-precio-${tmp.id}'), aumentarTotal('${tmp.id}')" class="product-mas">+</button>
                      </div>
                    </div>
                  </div>
                  <hr>`;

    // Se crea el contenedor hijo
    let cproduct = document.createElement("div");
    cproduct.setAttribute("class", "product");
    cproduct.setAttribute("id", "d-producto-" + tmp.id);
    cproduct.innerHTML = product;
    // Se agrega el contenedor hijo al padre
    contenedor.appendChild(cproduct);

    // Obtencion del total inicial
    totalCarrito();
  });
};

// Funcion que calcula el precio total de los productos que hay en el carrito
function totalCarrito() {
  let total = 0;
  let carrito = returnCarrito();
  // Se itera sobre el carrito y se obtiene el precio total de los productos en el carrito
  carrito.forEach(tmp => {
    total += tmp.precio;
  });
  // El total se pasa al HTML
  document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
};

// Funcion que reduce el total y la cantidad de un producto del carrito
function reducirTotal(idP) {
  let pre;

  // Se obtiene el carrito desde localStorage. En caso de no existir se un array vacio
  let carrito = JSON.parse(localStorage.getItem("carrito_local")) || [];

  // Se busca el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP){
      pre = tmp.precio;
    }
  });

  // Se busca el producto y se reduce su precio y cantidad si hay mas de 1 producto
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad > 1) {
        tmp.precio -= pre;
        tmp.cantidad -= 1;
      }
    }
  });

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
  
  // Se actualiza el total del carrito
  totalCarrito();
}

// Funcion que aumenta el total y la cantidad de un producto del carrito
function aumentarTotal(idP) {
  let pre;

  // Se obtiene el carrito desde localStorage. En caso de no existir se un array vacio
  let carrito = JSON.parse(localStorage.getItem("carrito_local")) || [];

  // Se busca el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP){
      pre = tmp.precio;
    }
  });

  // Se busca el producto y se aumenta su precio y cantidad si hay menos de 100 producto
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad < 100) {
        tmp.precio += pre;
        tmp.cantidad += 1;
      }
    }
  });

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
  
  // Se actualiza el total del carrito
  totalCarrito();
}

// Funcion que elimina un producto del carrito
function eliminar(idE) { 
  let carrito = returnCarrito();

  // Se obtiene la id
  let id = idE.substring(11);

  // Se busca la posicion del producto en el carrito, devuelve -1 si no se encuentra
  let index = carrito.findIndex(pro => pro.id === id);

  // Si se encuentra se borra del carrito
  if (index !== -1){
    carrito.splice(index, 1);

    // Se asigna una variable para el producto asociado a la id para poder borrarlo del HTML
    let producto = document.querySelector("#d-producto-" + id);
    let contenedor = document.getElementById("d-products");
    contenedor.removeChild(producto);

    // Se actualiza el contador del carrito
    del_Contador();
    loadContador();
    
    // Se actualiza el localStorage
    localStorage.setItem("carrito_local", JSON.stringify(carrito));
  };
  
  // Se actualiza el total
  totalCarrito();
};






