// Array de los productos
let productos = [];

// Se recuperan los datos de productos.json y se replican en el array
fetch("/json/productos.json")
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

// Array del carrito
let carrito = [];

// Funcion para ver si existe el producto en el carrito, devuelve true si lo encuentra
function exist(id) {
  return carrito.some(tmp => tmp.id === id);
};

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
  }
  else {
    id = idAdd.substring(4);
    // Obtencion del precio y la cantidad del producto elegido
    pre = document.querySelector("#h-precio-" + id).textContent;
    pre2 = parseInt(pre.substring(1));
    con = parseInt(document.querySelector("#h-contador-" + id).textContent);
  }

  // Iteracion para obtener los datos faltantes del producto a traves del json
  productos.forEach((tmp) => {
    if (tmp.id === id) {
      nom = tmp.nombre;
      img = tmp.imagen;
    }
  });
  
  // Obtencion del contador de productos del carrito
  shop_cont = parseInt(document.getElementById("shopping-contador").textContent);

  // Condicion que valida la existencia del producto en el carrito
  if (!exist(id)) {
    // Si no lo encuentra se crea un producto (Objeto)
    let producto = {
      id: id,
      nombre: nom,
      imagen: img,
      precio: pre2,
      cantidad: con
    };
    // Se añade el producto al carrito
    carrito.push(producto);
    // Se modifica el contador de productos del carrito
    document.getElementById("shopping-contador").textContent = shop_cont + 1;
  } else {
    // Si existe el producto en el carrito se le suma el precio y la cantidad elegida
    carrito.forEach((tmp) => {
      if (tmp.id === id) {
        tmp.precio += pre2;
        tmp.cantidad += con;
      };
    });
  };
};

// Funcion que despliega los productos agregados al carrito
function desplegar() {
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

  // Se itera sobre el carrito y se obtiene el precio total de los productos en el carrito
  carrito.forEach(tmp => {
    total += tmp.precio;
  });
  // El total se pasa al HTML
  document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
};

// Funcion que calcula el precio total cuando se descuentan productos desde el carrito
function reducirTotal(idP) {
  let total = 0;
  let precio;
  
  // Se itera sobre los productos para obtener el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP) {
      precio = parseInt(tmp.precio);
    };
  });

  // Se itera sobre el carrito y se reduce el precio y la cantidad del producto en el carrito
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad > 1) {
        tmp.cantidad -= 1;

        if (tmp.precio > precio) {
          tmp.precio -= precio;
        };
      };
    };

    // Se calcula el precio total de los productos en el carrito y se pasa al HTML
    total += tmp.precio;
    document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
  });
};

// Funcion que calcula el precio total cuando se aumentan productos desde el carrito
function aumentarTotal(idP) {
  let total = 0;
  let precio;
  
  // Se itera sobre los productos para obtener el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP) {
      precio = parseInt(tmp.precio);
    };
  });

  // Se itera sobre el carrito y se aumenta el precio y la cantidad del producto en el carrito
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad < 100) {
        tmp.cantidad += 1;

        if (tmp.precio < precio * 100) {
          tmp.precio += precio;
        };
      };
    };

    // Se calcula el precio total de los productos en el carrito y se pasa al HTML
    total += tmp.precio;
    document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
  });
};

// Funcion que elimina un producto del carrito
function eliminar(idE) { 
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

    // Obtencion del contador de productos del carrito
    shop_cont = parseInt(document.getElementById("shopping-contador").textContent);
    // Se modifica el contador de productos del carrito
    document.getElementById("shopping-contador").textContent = shop_cont - 1;
  };
  
  // Se actualiza el total
  totalCarrito();
}








