// Validaciones de Formulario

// Validacion del registro
function validaRegistro() {
  let rut = document.getElementById("rut-r").value;
  let nombres = document.getElementById("nombres-r").value;
  let paterno = document.getElementById("paterno-r").value;
  let materno = document.getElementById("materno-r").value;
  let telefono = document.getElementById("telefono-r").value;
  let direccion = document.getElementById("direccion-r").value;
  let correo = document.getElementById("correo-r").value;
  let contrasenia = document.getElementById("contrasenia-r").value;
  let contrasenia2 = document.getElementById("contrasenia-2-r").value;

  const boton = document.getElementById("submit-r");
  const contenedor = document.getElementById("unete-r");

  // Rut
  if (validarRut(rut)) {
    let input = document.getElementById("rut-r");
    correcto(input, contenedor, boton);
    // Nombres
    if (nombres.length >= 3 && nombres.length <= 30 && validarTexto(nombres)) {
      let input = document.getElementById("nombres-r");
      correcto(input, contenedor, boton);
      // Apellido paterno
      if (paterno.length >= 3 && paterno.length <= 30 && validarTexto(paterno)) {
        let input = document.getElementById("paterno-r");
        correcto(input, contenedor, boton);
        // Apellido materno
        if (materno.length >= 3 && materno.length <= 30 && validarTexto(materno)) {
          let input = document.getElementById("materno-r");
          correcto(input, contenedor, boton);
          // Telefono
          if (validarTelefono(telefono)) {
            let input = document.getElementById("telefono-r");
            correcto(input, contenedor, boton);
            // Dirección
            if (direccion.length >= 5 && direccion.length <= 100) {
              let input = document.getElementById("direccion-r");
              correcto(input, contenedor, boton);
              // Correo
              if (validarCorreo(correo)) {
                let input = document.getElementById("correo-r");
                correcto(input, contenedor, boton);
                // Contraseña
                if (validarContrasenia(contrasenia)) {
                  let input = document.getElementById("contrasenia-r");
                  correcto(input, contenedor, boton);
                  // Confirmacion contraseña
                  if (contrasenia2 === contrasenia) {
                    let input = document.getElementById("contrasenia-2-r");
                    correcto(input, contenedor, boton);
                  } else {
                    let input = document.getElementById("contrasenia-2-r");
                    let texto = "Las contraseñas no coinciden.";
                    error(input, contenedor, texto, boton);
                  }
                } else {
                  let input = document.getElementById("contrasenia-r");
                  let texto = "Contraseña no valida. Minimo 8 caracteres y debe contener letras y numeros.";
                  error(input, contenedor, texto, boton);
                }
              } else {
                let input = document.getElementById("correo-r");
                let texto = "Formato de correo no valido. Debe contener '@' y una direccion valida.";
                error(input, contenedor, texto, boton);
              }
            }
            else {
              let input = document.getElementById("direccion-r");
              let texto = "Dirección no válida. Mínimo 5 carácteres y máximo 100.";
              error(input, contenedor, texto, boton);
            }
          }
          else {
            let input = document.getElementById("telefono-r");
            let texto = "Teléfono no válido. Mínimo 8 digitos y recuerda agregar el 9 al principio.";
            error(input, contenedor, texto, boton);
          }
        } else {
          let input = document.getElementById("materno-r");
          let texto = "Apellido no válido. Mínimo 3 letras y máximo 30.";
          error(input, contenedor, texto, boton);
        }
      } else {
        let input = document.getElementById("paterno-r");
        let texto = "Apellido no válido. Mínimo 3 letras y máximo 30.";
        error(input, contenedor, texto, boton);
      }
    } else {
      let input = document.getElementById("nombres-r");
      let texto = "Nombre no válido. Mínimo 3 letras y máximo 30.";
      error(input, contenedor, texto, boton);
    }
  } else {
    let input = document.getElementById("rut-r");
    let texto = "Formato de rut no válido. Ingrese el rut sin puntos y con guión.";
    error(input, contenedor, texto, boton);
  }
}

// Validacion del login
function validarLogin() {
  let correo = document.getElementById("correo-l").value;
  let contrasenia = document.getElementById("contrasenia-l").value;

  const boton = document.getElementById("submit-l");
  const contenedor = document.getElementById("unete-l");

  // Correo
  if (validarCorreo(correo)) {
    let input = document.getElementById("correo-l");
    correcto(input, contenedor, boton);
    // Contraseña
    if (validarContrasenia(contrasenia)) {
      let input = document.getElementById("contrasenia-l");
      correcto(input, contenedor, boton);
    } else {
      let input = document.getElementById("contrasenia-l");
      let texto =
        "Contraseña no valida. Minimo 8 caracteres y debe contener letras y numeros.";
      error(input, contenedor, texto, boton);
    }
  } else {
    let input = document.getElementById("correo-l");
    let texto =
      "Formato de correo no valido. Debe contener '@' y una direccion valida.";
    error(input, contenedor, texto, boton);
  }
}

// Validacion de la Id del seguimiento - min 1 digito - max 4 digitos
function validarSeguimiento() {
  let idS = document.getElementById("seguimiento-s").value;
  const boton = document.getElementById("submit-s");

  if (!validarIdSeguimiento(idS)) {
    let input = document.getElementById("seguimiento-s");
    let contenedor = document.getElementById("c-seguimiento-s");
    let texto =
      "Id del seguimiento debe contener solo numeros y estar entre 1 y 4 digitos.";

    error(input, contenedor, texto, boton);
  } else {
    document.getElementById("seguimiento-s").style.border =
      "0.188rem solid #436A6F";
    document.getElementById("c-seguimiento-s").innerHTML =
      "<div class='alert alert-success w-100 mx-auto text-center'> " +
      "Pedido encontrado (Mensaje provisorio) </div>";
  }
}

// Validacion del correo para el cambio de contraseña
function validarCambio() {
  let correo = document.getElementById("correo-c").value;
  const boton = document.getElementById("submit-c");

  if (!validarCorreo(correo)) {
    let input = document.getElementById("correo-c");
    let contenedor = document.getElementById("contenedor-c");
    let texto =
      "Formato de correo no valido. Debe contener '@' y una direccion valida.";

    error(input, contenedor, texto, boton);
  } else {
    document.getElementById("correo-c").style.border = "0.188rem solid #436A6F";
    document.getElementById("contenedor-c").innerHTML =
      "<div class='alert alert-success w-100 mx-auto text-center'> " +
      "Correo enviado exitosamente.";
  }
}

// Funcion que pasa mensajes de error en los formularios
function error(idInput, idContenedor, textoError, idBoton) {
  idBoton.setAttribute("type", "button");
  idInput.style.border = "0.188rem solid red";
  idContenedor.innerHTML =
    "<div class='alert alert-danger w-50 mx-auto text-center'> " +
    textoError +
    "</div>";
}

// Funcion que confirma los pasos
function correcto(idInput, idContenedor, idBoton) {
  idBoton.setAttribute("type", "submit");
  idInput.style.border = "0.188rem solid black";
  idContenedor.innerHTML = "";
}

// Expresiones regulares
function validarRut(rut) {
  let re = /^\d{7,8}-[\dkK]$/;
  return re.test(rut);
}

function validarTexto(texto) {
  let re = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;
  return re.test(texto);
}

function validarContrasenia(contrasenia) {
  let re = /^(?=.*\d)(?=.*[a-zA-ZáéíóúÁÉÍÓÚñÑ]).{8,}$/;
  return re.test(contrasenia);
}

function validarCorreo(correo) {
  let re = /^[a-zA-Z0-9._%+-]+@(gmail\.com|outlook\.com)$/i;
  return re.test(correo);
}

function validarTelefono(telefono) {
  let re = /^\+?[9]\d{8,}$/;
  return re.test(telefono);
}

// Permite solo numeros - min 1 digito - max 4 digitos
function validarIdSeguimiento(id) {
  let re = /^[0-9]\d{0,3}$/;
  return re.test(id);
}
