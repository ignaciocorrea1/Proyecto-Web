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
};

// Funcion que reduce el contador del carrito del localStorage
function del_Contador(){
  // Se obtiene el contador desde el localStorage. En caso de no existir devolverá 0
  let contLocal = JSON.parse(localStorage.getItem("carrito_contador")) || 0;

  let contAct = contLocal - 1; 
  // Se actualiza el localStorage
  localStorage.setItem("carrito_contador", JSON.stringify(contAct));
};

// Funcion que retorna el contador de productos del carrito
function returnContador(){
  return contador = JSON.parse(localStorage.getItem("carrito_contador")) || 0;
};

// Funcion que carga el contador
function loadContador(){
  let contador = returnContador();
  document.getElementById("shopping-contador").textContent = contador;
};

// Se actualiza en el HTML el contador de productos del carrito
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
  };

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
};

// Funcion que retorna el carrito
function returnCarrito(){
  return JSON.parse(localStorage.getItem("carrito_local")) || [];
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

// Funcion que despliega los productos agregados al carrito en el offcanva
function desplegar() {
  // Se trae el carrito
  let carrito = returnCarrito();

  // Se limpia el carrito
  let contenedor = document.getElementById("d-products");
  contenedor.innerHTML = "";

  // Se recorre el carrrito para desplegar en el HTML todo lo que este ahi
  carrito.forEach(tmp => {
    /* Se crea una variable para se usan template literals para incrustar los datos al HTML de una manera mas eficiente,
       tambien se evitan conflictos con las funciones del onclick. Las plantillas permiten insertar variables y expresiones 
       dentro de las llaves ${} se usan `` para abrirlas y cerrarlas
    */
    let product = `<div class="product-container">
                    <div class="product-desc">
                      <h2>${tmp.nombre}</h2>
                      <img src="${tmp.imagen}" alt="Cargando imagen...">
                      <button onclick="eliminar('d-eliminar-${tmp.id}', 'offcanva')" class="product-remove" id="d-eliminar-${tmp.id}">Eliminar</button>
                    </div>
                    <div class="product-desc-2">
                      <div class="product-price">
                        <span class="precio">Precio:</span>
                        <span class="precio-2" id="d-precio-${tmp.id}">$${tmp.precio}</span>
                      </div>
                      <div class="product-add">
                        <button onclick="menos('d-contador-${tmp.id}', 'd-precio-${tmp.id}'), reducirTotal('${tmp.id}', 'offcanva')" class="product-menos">-</button>
                        <span class='product-contador' id='d-contador-${tmp.id}'>${tmp.cantidad}</span>
                        <button onclick="mas('d-contador-${tmp.id}', 'd-precio-${tmp.id}'), aumentarTotal('${tmp.id}', 'offcanva')" class="product-mas">+</button>
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

    // Obtencion del total
    totalCarrito("offcanva");
  });
};

// Funcion que despliega los productos agregados al carrito en la vista general
function desplegado(){
  try {
    // Se trae el carrito 
    let carrito = returnCarrito();

    // Se limpia el carrito
    let contenedor = document.getElementById("dd-products");
    contenedor.innerHTML = "";

    // Se recorre el carrito para desplegar en el HTML lo que este ahi
    carrito.forEach(tmp => {
      // Se crea una variable
      let producto = `<div class="carrod-container">
                        <div class="carro-inf">
                          <img src="${tmp.imagen}" alt="Cargando imagen..."/>
                          <div class="carro-desc">
                            <h2>${tmp.nombre}</h2>
                            <div class="carro-buttons">
                              <button onclick="menos('c-contador-${tmp.id}', 'c-precio-${tmp.id}'), reducirTotal('${tmp.id}', 'vista')" class="carro-menos">-</button>
                              <span class="carro-contador" id='c-contador-${tmp.id}'>${tmp.cantidad}</span>
                              <button onclick="mas('c-contador-${tmp.id}', 'c-precio-${tmp.id}'), aumentarTotal('${tmp.id}', 'vista')" class="carro-mas">+</button>
                            </div>
                          </div>
                        </div>
                        <div class="carro-total">
                          <h2>Total</h2>
                          <span  id="c-precio-${tmp.id}">$${tmp.precio}</span>
                        </div>
                        <button class="carro-eliminar" onclick="eliminar('c-eliminar-${tmp.id}', 'vista')">Eliminar</button>
                      </div>
                      <hr>`;

      // Se crea el contenedor hijo
      let cproduct = document.createElement("div");
      cproduct.setAttribute("class", "dd-product");
      cproduct.setAttribute("id", "c-producto-" + tmp.id);
      cproduct.innerHTML = producto;
      // Se agrega el contenedor hijo al padre
      contenedor.appendChild(cproduct);
      
      // Se obtiene el total
      totalCarrito("vista");

    });
  } catch (error) {
    
  };
};

/* El desplegar los productos se tuvo que hacer de esta forma ya que al intentar hacer que se desplieguen solo al hacer click 
   en el boton de "Ir al carro" daba problemas (Si el button estaba sin el <a> se desplegaba bien pero, no se redirigia a la
   pagina, probé el redirigirlo por JS pero no funcionó, en resumen el <a> daba problemas). Tambien el contenedor.innerHTML 
   daba problemas asi que para evitarlos se encerró gran parte de la funcion en un trycatchonclick='selectMetodo()' 
*/ 

// Se despliega el carrito en la vista de carrito
document.addEventListener("DOMContentLoaded", () => {
  desplegado();
});

// Evento al hacer click fuera del offcanva para cerrarlo
document.addEventListener('DOMContentLoaded', () => {
  // Se obtiene la id del offcanva
  let offcanva = document.getElementById("offcanvasRight");

  // Se le agrega el evento
  offcanva.addEventListener('hidden.bs.offcanvas', () => {
    desplegado();
    // Se agrega esta funcion para que actulice el total despues de cerrar el offcanva y asi no exista la necesidad de recargar
    // la pagina, esto por si el usuario se encuentra ya en la vista del carro y elimina un producto desde el offcanva
    totalCarrito("vista");
  });
});

// Funcion que calcula el precio total de los productos que hay en el carrito
function totalCarrito(zona) {
  let total = 0;
  let carrito = returnCarrito();
  // Se itera sobre el carrito y se obtiene el precio total de los productos en el carrito
  carrito.forEach(tmp => {
    total += tmp.precio;
  });
  // El total se pasa al HTML
  if (zona === "offcanva"){
    document.getElementById("producto-total").textContent = "Total a pagar: $" + total;
  } else if (zona === "vista"){
    document.getElementById("carro-total").textContent = "$" + total;
  } else {
    document.getElementById("resumen-total").textContent = "$" + total;
  };
};

// Funcion que reduce el total y la cantidad de un producto del carrito
function reducirTotal(idP, zona) {
  let pre;

  // Se obtiene el carrito desde localStorage. En caso de no existir se un array vacio
  let carrito = returnCarrito();

  // Se busca el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP){
      pre = tmp.precio;
    };
  });

  // Se busca el producto y se reduce su precio y cantidad si hay mas de 1 producto
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad > 1) {
        tmp.precio -= pre;
        tmp.cantidad -= 1;
      };
    };
  });

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
  
  // Se actualiza el total del carrito
  totalCarrito(zona);
}

// Funcion que aumenta el total y la cantidad de un producto del carrito
function aumentarTotal(idP, zona) {
  let pre;

  // Se obtiene el carrito desde localStorage. En caso de no existir se un array vacio
  let carrito = returnCarrito();

  // Se busca el precio base del producto
  productos.forEach(tmp => {
    if (tmp.id === idP){
      pre = tmp.precio;
    };
  });

  // Se busca el producto y se aumenta su precio y cantidad si hay menos de 100 producto
  carrito.forEach(tmp => {
    if (tmp.id === idP) {
      if (tmp.cantidad < 100) {
        tmp.precio += pre;
        tmp.cantidad += 1;
      };
    };
  });

  // Se actualiza el localStorage
  localStorage.setItem("carrito_local", JSON.stringify(carrito));
  
  // Se actualiza el total del carrito
  totalCarrito(zona);
}

// Funcion que elimina un producto del carrito
function eliminar(idE, zona) { 
  let carrito = returnCarrito();

  // Se obtiene la id
  let id = idE.substring(11);

  // Se busca la posicion del producto en el carrito, devuelve -1 si no se encuentra
  let index = carrito.findIndex(pro => pro.id === id);

  // Si se encuentra se borra del carrito
  if (index !== -1){
    carrito.splice(index, 1);

    if (zona === "offcanva") {
      // Se asigna una variable para el producto asociado a la id para poder borrarlo del offcanva
      let producto = document.querySelector("#d-producto-" + id);
      let contenedor = document.getElementById("d-products");
      contenedor.removeChild(producto);
    } else {
      // Se asigna una variable para el producto asociado a la id para poder borrarlo de la vista del carrito
      let producto2 = document.querySelector("#c-producto-" + id);
      let contenedor2 = document.getElementById("dd-products");
      contenedor2.removeChild(producto2);
    };

    // Se actualiza el contador del carrito
    del_Contador();
    loadContador();

    // Se actualiza el localStorage
    localStorage.setItem("carrito_local", JSON.stringify(carrito));
  };
  
  // Se actualiza el total
  totalCarrito(zona);
  // Se agrega esta funcion para que actualice los productos de la vista del carro al eliminarlos, esto por si el usuario 
  // se encuentra ya en la vista del carro pero, elimina un producto desde el offcanva
  desplegado();
};

// Proceso de pago

// Funcion que muestra el resumen del pedido
function resumenPedido(){
  try {
    // Se trae el carrito
    let carrito = returnCarrito();

    // Se limpia el contenedor
    let contenedor = document.getElementById("productos-container");
    contenedor.innerHTML = "";

    // Se recorre el carrito para desplegar los productos
    carrito.forEach(tmp => {
      // Se crea una variable
      let producto = `<div class="producto-r">
                          <div class="product-desc">
                            <h3>${tmp.nombre}</h3>
                            <img src="${tmp.imagen}" alt="Cargando imagen...">
                          </div>
                          <div class="product-desc-2">
                            <div class="product-price">
                              <span class="precio">Precio:</span>
                              <span class="precio-2">$${tmp.precio}</span>
                            </div>
                            <div class="product-count">
                              <span class="product-condesc">Cantidad:</span>
                              <span class="product-contador">${tmp.cantidad}</span>
                            </div>
                          </div>
                          <hr>
                      </div>`;

      // Se crea el contenedor hijo
      let rproducto = document.createElement("div");
      rproducto.setAttribute("class", "producto-res");
      rproducto.setAttribute("id", "r-producto-" + tmp.id);
      rproducto.innerHTML = producto;
      // Se agrega al contenedor
      contenedor.appendChild(rproducto);

      // Se obtiene el total del pedido
      totalCarrito("resumen");
    });
  } catch (error) {
    
  }
}

// Se carga el resumen - por la misma razon que con desplegado(), la funcion resumenPedido() tambien se encierra en un trycatch
document.addEventListener("DOMContentLoaded", () => {
  resumenPedido();
});

// Funcion que valida la existencia de productos en el carrito
function validaCarro(zona) {
  // Se trae el carrito
  let carrito = returnCarrito();

  // Se valida que exista como minimo 1 producto en el carrito
  if (carrito.length === 0) {
    // Se crea un mensaje para el usuario
    let vacio = "<span>Tu carro aún está vacío</span>";

    if (zona === "vista"){
      // Se busca el contenedor del carro
      let contenedor = document.getElementById("dd-products");
      contenedor.innerHTML = "";
  
      // Se crea un contenedor hijo
      let cvacio = document.createElement("div");
      cvacio.setAttribute("class", "carro-msg");
      cvacio.innerHTML = vacio;
      // Se agrega al contenedor principal
      contenedor.appendChild(cvacio);
      
      // Se busca el <a> y se le cambia su href para que no redireccione al pago
      let a = document.getElementById("a-inipago");
      a.setAttribute("href", "#")
    } else {
      // Se busca el contenedor del offcanva
      let contenedor = document.getElementById("d-products");
      contenedor.innerHTML = "";
  
      // Se crea un contenedor hijo
      let cvacio = document.createElement("div");
      cvacio.setAttribute("class", "offcanva-msg");
      cvacio.innerHTML = vacio;
      // Se agrega al contenedor principal
      contenedor.appendChild(cvacio);
      
      // Se busca el <a> y se le cambia su href para que no redireccione al pago
      let a = document.getElementById("o-inipago");
      a.setAttribute("href", "#")
    }
  } else {
    if (zona === "vista"){
      // Se busca el <a> y se le cambia su href para que redireccione al pago
      let a = document.getElementById("a-inipago");
      a.setAttribute("href", "/accounts/pago");
    } else {
      // Se busca el <a> y se le cambia su href para que redireccione al pago
      let a = document.getElementById("o-inipago");
      a.setAttribute("href", "/accounts/pago");
    }
  }
}

// Funcion para validar los pasos del proceso de pago
function validaPasos(paso) {
  // Se valida el primer paso
  if (paso === 1 && validaPaso1()) {
    // Se cambia el indicador del paso
    document.getElementById("paso-indicador-1").innerHTML = "";
    document.getElementById("paso-indicador-2").innerHTML = "<span class='material-symbols-outlined done'>" +
                                                              "done" +
                                                            "</span>";

    // Se oculta el primer paso y se muestra el segundo
    document.getElementById("paso-compra-1").setAttribute("hidden", true);
    document.getElementById("paso-compra-2").removeAttribute("hidden");

  } else if (paso === 2 && validaPaso2()) {
    // Se cambia el indicador del paso
    document.getElementById("paso-indicador-1").innerHTML = "";
    document.getElementById("paso-indicador-2").innerHTML = "<span class='material-symbols-outlined done'>" +
                                                              "done" +
                                                            "</span>";

    // Se oculta el segundo paso y se muestra el tercero
    document.getElementById("paso-compra-2").setAttribute("hidden", true);
    document.getElementById("paso-compra-3").removeAttribute("hidden");

  } else if (paso === 3 && validaPaso3()) {
    // Se cambia el indicador del paso
    document.getElementById("paso-indicador-2").innerHTML = "";
    document.getElementById("paso-indicador-3").innerHTML = "<span class='material-symbols-outlined done'>" +
                                                              "done" +
                                                            "</span>";

    // Se oculta el tercer paso y se muestra el cuarto paso
    document.getElementById("paso-compra-3").setAttribute("hidden", true);
    document.getElementById("paso-compra-4").removeAttribute("hidden");
  }
};

// Funcion que valida el primer paso del proceso de pago
function validaPaso1() {
  // Se traen los datos
  let nombres = document.getElementById("nombre-paso").value;
  let rut = document.getElementById("rut-paso").value;
  let correo = document.getElementById("correo-paso").value;
  let telefono = document.getElementById("telefono-paso").value;
  let direccion = document.getElementById("direccion-paso").value;

  // Si todos los campos estan completados devolverá true, sino mostrará un mensaje de error
  if (nombres.length > 0) {
    if (rut.length > 0) {
      if (correo.length > 0) {
        if (telefono.length > 0) {
          if (direccion.length > 0) {
            return true;
          }else {
            errorPaso(1, "La direccion esta vacia.");
            return false;
          };
        }else {
          errorPaso(1, "El telefono esta vacio.");
          return false;
        };
      }else {
        errorPaso(1, "El correo esta vacio.");
        return false;
      };
    }else {
      errorPaso(1, "El rut esta vacio.");
      return false;
    };
  }else {
    errorPaso(1, "El nombre esta vacio.");
    return false;
  };
};

// Funcion que valida el segundo paso del proceso de pago
function validaPaso2() {
  // Se valida que un metodo este seleccionado
  if (!document.getElementById("metodo-1").checked && 
      !document.getElementById("metodo-2").checked &&
      !document.getElementById("metodo-3").checked && 
      !document.getElementById("metodo-4").checked &&
      !document.getElementById("metodo-5").checked) {
    errorPaso(2, "No se eligió un método");
    return false;
  }else {
    return true;
  };
};

// Funcion que valida el tercer paso del proceso de pago
function validaPaso3() {
  let tarjeta = document.getElementById("tarjeta-paso").value;

  // Si el campo esta completado devolverá true
  if (tarjeta.length > 0) {
    return true;
  } else {
    errorPaso(3, "El Nro. de tarjeta esta vacio");
    return false;
  }
}

// Funcion que envia los productos del carrito a un json externo
function importCarro() {
  // Se trae el carrito
  let carrito = returnCarrito();

  // console.log(carrito)

  // Se realiza una solicitud para enviar los productos a la ruta indicada en el fetch()
  fetch("/CoffeKong/load_carrito", {
    // Se indica el metodo, el tipo de contenido(formato json), y el token 
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getToken()
    },
    // Convierte el carrito en una cadena Json
    body: JSON.stringify(carrito)
  })
};

// Funcion para obtener el token de las cookies
// Funcion creada porque daba el siguiente error al tratar de enviar el carrito: 
// Forbidden (CSRF token missing.): /CoffeKong/load_carrito
function getToken() {
  // Se acceden a las cookies del documento, se dividen por un ; y se itera sobre ellas para encontrar el token
  const cookie = document.cookie.split('; ').find(cookie => cookie.startsWith('csrftoken='));
  // Si lo encuentra devolvera "csrftoken=" por lo que hay que quitarle el = 
  // El csrftoken= se podria decir que es un sufijo que usan algunos frameworks para identificar los tokens
  if (cookie) {
    // Se retorna el token
    return cookie.split('=')[1];
  }
  // Si no lo encuentra devolvera null
  return null;
};

// Funcion que mostrara un mensaje de error al usuario
function errorPaso(nro, msg) {
  if (nro === 1) {
    // Se busca el contenedor
    document.getElementById("paso-msg-1").setAttribute("class", "alert alert-danger w-80 mx-auto text-center");
    document.getElementById("paso-msg-1").setAttribute("style", "font-size: 0.8em;");
    document.getElementById("paso-msg-1").innerHTML = msg;
  } else if (nro === 2) {
    // Se busca el contenedor
    document.getElementById("paso-msg-2").setAttribute("class", "alert alert-danger w-50 text-center");
    document.getElementById("paso-msg-2").setAttribute("style", "font-size: 0.8em; margin-left: 10vw;");
    document.getElementById("paso-msg-2").innerHTML = msg;
  } else if (nro === 3) {
    // Se busca el contenedor
    document.getElementById("paso-msg-3").setAttribute("class", "alert alert-danger w-80 text-center");
    document.getElementById("paso-msg-3").setAttribute("style", "font-size: 0.8em;");
    document.getElementById("paso-msg-3").innerHTML = msg;
  }
};

// Funcion que cambia el color de los metodos de pago al seleccionarlos
function selectMetodo() {
  // Se valida que solo un metodo este seleccionado
  if (document.getElementById("metodo-1").checked) {

  } else if (document.getElementById("metodo-2").checked) {
    
  } else if (document.getElementById("metodo-3").checked) {
    
  } else if (document.getElementById("metodo-4").checked) {
    
  } else if (document.getElementById("metodo-5").checked) {
    
  }
};

// Funcion que retorna los pasos del proceso de pago
function pasos(nro) {
  if (nro === 1 ) {
    // Paso 1 - Datos del cliente
    let paso = "<div class='pago-datos'>" +
                  "<div class='form'" +
                        "<input class='form-input' type='text' id='nombre-paso' value={{cliente.nombres}} placeholder='Nombre (*)' required >" +
                        "<input class='form-input' type='text' id='rut-paso' value={{cliente.run}} placeholder='Rut (*)' required >" +
                        "<input class='form-input' type='email' id='correo-paso' value={{cliente.correo}} placeholder='Correo (*)' required >" +
                        "<input class='form-input' type='text' id='telefono-paso' value={{cliente.telefono}} placeholder='Teléfono (*)' required >" +
                        "<input class='form-input' type='text' id='direccion-paso' value={{cliente.direccion}} placeholder='Dirección de entrega (*)' required >" +
                        "<div id='paso-msg'></div>" +
                        "<input class='form-submit' type='button' value='Aceptar' onclick='validaPasos(1)' >" +
                  "</div>" +
                "</div>";
    return paso;
  } else if (nro === 2) {
    // Paso 2 - Metodo de pago
    let paso =  "<div class='pago-metodo'>" +
                    "<div class='pago-option'>" +
                      "<div class='pago-group'>" +
                        "<input type='radio' class='m-radio' id='metodo-1' name='metodo' ></input>" +
                        "<label for='metodo-1' class='m-pago' >Transferencia o depósito bancario</label>" +
                      "</div>" +

                      "<div class='pago-group'>" +
                        "<input type='radio' class='m-radio' id='metodo-2' name='metodo' ></input>" +
                        "<label for='metodo-2' class='m-pago' >Botón de pago Banco Estado</label>" +
                      "</div>" +

                      "<div class='pago-group'>" +
                        "<input type='radio' class='m-radio' id='metodo-3' name='metodo' ></input>" +
                        "<label for='metodo-3' class='m-pago' >Botón de pago Banco Santander</label>" +
                      "</div>" +

                      "<div class='pago-group'>" +
                        "<input type='radio' class='m-radio' id='metodo-4' name='metodo' ></input>" +
                        "<label for='metodo-4'' class='m-pago' >Webpay</label>" +
                      "</div>" +

                      "<div class='pago-group'>" +
                        "<input type='radio' class='m-radio' id='metodo-5' name='metodo' ></input>" +
                        "<label for='metodo-5' class='m-pago' >Mercado Pago</label>" +
                      "</div>" +
                      
                    "</div>" +
                    "<div id='paso-msg'></div>" +
                    "<input type='button' class='m-pago-cont' value='Aceptar' onclick='validaPasos(2)' ></input>" +
                "</div>";
    return paso;
  } else if (nro === 3) {
    // Paso 3 - Tarjeta del cliente
    let paso =  "<div class='pago-datos'>" +
                  "<div class='form'>" +
                      "<input class='form-input' type='number' id='tarjeta-paso' placeholder='Nro. de tarjeta (*)' required >" +
                      "<div id='paso-msg'></div>" +
                      "<input class='form-submit' type='button' value='Aceptar' onclick='validaPasos(3)' >" +
                  "</div>" +
                "</div>";
    return paso;
  } else {
    // Paso 4 - Confirmacion de la compra
    let paso = "<div class='pago-details'>" +
                  "<table class='table-detail'>" +
                    "<tr>" +
                      "<th>Dirección de entrega</th> <th class='dos-p'>:</th> <td>" + document.getElementById("direccion-paso").value + " </td>" +
                    "</tr>" +
                    
                    "<tr>" +
                      "<th>Destinatario</th> <th class='dos-p'>:</th> <td>" + document.getElementById("nombre-paso").value + " </td>" +
                    "</tr>" +
                    
                    "<tr>" +
                      "<th>Rut</th> <th class='dos-p'>:</th> <td>" + document.getElementById("rut-paso").value + " </td>" +
                    "</tr>" +
                    
                    "<tr>" +
                      "<th>Teléfono</th> <th class='dos-p'>:</th> <td>" + document.getElementById("telefono-paso").value + " </td>  " +
                    "</tr>" +

                  "</table>" +
                  "<button class='button-pagar'>Pagar</button>" +
                "</div>";
    return paso;
  };
};
