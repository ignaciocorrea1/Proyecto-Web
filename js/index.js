// Funciones para los contadores

// Funcion para quitarle 1 al contador y restarle al precio
function menos(idCont, idPrecio) {
    // Obtencion del numero del contador
    let contador = document.querySelector("#" + idCont);
    let cont = parseInt(contador.textContent);

    // Obtencion del precio
    let prod = document.querySelector("#" + idPrecio);
    let precio = parseInt(prod.textContent);

    // Validar si el contador es mayor a 10
    if (cont > 1) {
        cont--;

        // Calculo del precio total del producto
        let total = precio * cont;
        console.log(cont, total);

        // Asignacion de valores
        contador.textContent = cont.toString();
        prod.textContent = total.toString();
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
        prod.textContent = total.toString();
    }
    else {
        alert("El maximo es 10");
    };
};










