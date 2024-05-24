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
  let id = idC.substring(11); 
  
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
  let id = idC.substring(11); 

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

// Funcion para reestablecer el precio del producto y en 1 el contador sobre el modal
function reestablecer(idM) {
  // Substring a la id del modal para recuperar el precio y contador asociados a ese modal
  let id = idM.substring(6);

  // La iteracion busca en el json el precio asociado a la id y lo obtenido se setea
  productos.forEach((tmp) => {
    if (tmp.id === id) {
      document.querySelector("#h-precio-" + id).textContent = "$" + tmp.precio;
      document.querySelector("#h-contador-" + id).textContent = 1;
    }
  });
}

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
})

// Funciones del carrito

// Array del carrito
let carrito = [];

// Funcion para ver si existe el producto en el carrito
function exist(id) {
  return carrito.some(tmp => tmp.id === id);
}

// Funcion para agregar productos al carrito
function agregar(idAdd) {
  // Variables
  let id = idAdd.substring(4);
  let pre;
  let pre2;
  let con;
  let nom;
  let img;

  // Iteracion para obtener los datos faltantes del json
  productos.forEach((tmp) => {
    if (tmp.id === id) {
      nom = tmp.nombre;
      img = tmp.imagen;
    }
  });

  // Datos que provienen del HTML
  pre = document.querySelector("#h-precio-" + id).textContent;
  pre2 = parseInt(pre.substring(1));
  con = parseInt(document.querySelector("#h-contador-" + id).textContent);

  // Condicion que valida la existencia del producto en el carrito
  if (!exist(id)) {
    // Creacion de un objeto
    let producto = {
      id: id,
      nombre: nom,
      imagen: img,
      precio: pre2,
      cantidad: con,
    };
    // Se añade el objeto al array
    carrito.push(producto);
  } else {
    carrito.forEach((tmp) => {
      if (tmp.id === id) {
        tmp.precio += pre2;
        tmp.cantidad += con;
      }
    });
  }
}

// Funcion que despliega los productos agregados al carrito
function desplegar() {
  // Se limpia el carrito
  let contenedor = document.getElementById("d-products");
  contenedor.innerHTML = "";

  // Se recorre el array para desplegar en el html todo lo que este ahi
  carrito.forEach(tmp => {
    // Se usan template literals para incrustar los datos al HTML de una manera mas eficiente,
    // tambien se evitan conflictos con las funciones del onclick.
    // Las plantillas permiten insertar variables y expresiones dentro de las llaves ${} se usan
    // `` para abrirlas y cerrarlas
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
                        <button onclick="mas('d-contador-${tmp.id}', 'd-precio-${tmp.id}')" class="product-mas">+</button>
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

    // Desplegar el total inicial
    totalCarrito()
  });
}

// Funcion que elimina un producto del carrito
function eliminar(idE) { 
  // Se obtiene la id
  let id;
  
  if (idE.length == 12) {
    id = idE.substring(11, 12);
  } else if (idE.length == 13) {
    id = idE.substring(11, 13);
  }
  
  // Se busca la posision del producto en el carrito - devuelve -1 si no se encuentra nada
  let index = carrito.findIndex(pro => pro.id === id);

  // Si se encuentra se borra
  if (index !== -1){
    carrito.splice(index, 1);
    let producto = document.querySelector("#d-producto-" + id);
    let contenedor = document.getElementById("d-products");
    contenedor.removeChild(producto);
  }
}

// Funcion que calcula el total de lo que hay en el carrito
function totalCarrito() {
  let total = 0;

  carrito.forEach(tmp => {
    total += tmp.precio;
  });
  document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
}
/*
function reducirTotal(idP) {
  let total = 0;
  let precio;
  let cantidad = parseInt(document.getElementById("d-contador-" + idP).textContent);

  productos.forEach(tmp => {
    if (tmp.id === idP) {
      precio = tmp.precio;
      console.log("Precio del producto: "+ precio)
    }
  });

  carrito.forEach(tmp => {
    total += tmp.precio - precio;
    console.log("Total: "+ total)
  });
  document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
}
*/
/*
function reducirTotal(idP) {
  let total = 0;
  let descuento = 0;
  let proTotal;

  productos.forEach(tmp => {
    if (tmp.id === idP) {
      let precio = tmp.precio;
      let cantidad = parseInt(document.getElementById("d-contador-" + idP).textContent);
      
      if (cantidad > 1) {
        proTotal = precio * cantidad;
        console.log("Precio del producto: "+ precio)
        console.log("Cantidad del producto: "+ cantidad)
        console.log("Total del producto: "+ proTotal)
      }
    }
  });

  carrito.forEach(tmp => {
    descuento += tmp.precio - proTotal;
    console.log("Descuento: "+ descuento)
    total += tmp.precio - descuento;
    console.log("Total: "+ total2)
  });
  document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
}
*/










