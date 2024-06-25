from django.shortcuts import render, redirect
from .models import cliente, vendedor, tarjeta, pedido, tipoProducto, producto, detallePedido
import json

# Create your views here.
def index(request):
    context = {}
    # import_data()
    return render(request, "pages/index.html", context)

def menu(request):
    context = {}
    return render(request, "pages/menu.html", context)

""" Función para importar los productos del Json a la BD 
def import_data():
    try:
        # Se leen los datos
        with open('CoffeKong/static/json/productos.json', 'r', encoding='utf-8') as json_file:
            # Se crea y se asigna un diccionario a "productos"
            productos = json.load(json_file)
            # Se recorren los datos para crear los "tipoProductos"
            for tp in productos:
                tp = tipoProducto.objects.create(
                    id_tipoproducto = tp["tipo"],
                    descripcion = "Bebida" if tp["tipo"] == "b" else "Comida"
                )
                tp.save()

            # Se recorren los datos para crear los "productos"
            for p in productos:
                # Se crea un objeto y se manda a la BD
                p = producto.objects.create(
                    id_producto = p["id"],
                    nombre = p["nombre"],
                    descripcion = p["descripcion"],
                    precio = p["precio"],
                    imagen = p["imagen"],
                    tipo = p["tipo"]
                )
                p.save()
                productos.close()
                
    except Exception as e:
        print("Error al cargar el Json", e)
"""

def unete(request):
    context = {}
    return render(request, "pages/unete.html", context)

def seguimiento(request):
    context = {}
    return render(request, "pages/seguimiento.html", context)

def seguimiento2(request):
    context = {}
    return render(request, "pages/seguimiento2.html", context)

def carrito(request):
    context = {}
    return render(request, "pages/carrito.html", context)

def pago(request):
    context = {}
    return render(request, "pages/pago.html", context)

def ingreso(request):
    context = {}
    return render(request, "pages/ingreso.html", context)

def contrasenia(request):
    context = {}
    return render(request, "pages/contrasenia.html", context)

def historial(request):
    context = {}
    return render(request, "pages/historial.html", context)

def detalle(request):
    context = {}
    return render(request, "pages/detalle.html", context)

""" Crud """
def crud(request):
    vendedores = vendedor.objects.all()
    clientes = cliente.objects.all()
    tarjetas = tarjeta.objects.all()
    pedidos = pedido.objects.all()
    detallePedidos = detallePedido.objects.all()
    productos = producto.objects.all()
    tipoProductos = tipoProducto.objects.all()
    context = {
        "vendedores": vendedores,
        "clientes": clientes,
        "tarjetas": tarjetas,
        "pedidos": pedidos,
        "detallePedidos": detallePedidos,
        "productos": productos,
        "tipoProductos": tipoProductos,
    }
    return render(request, "pages/crud/crud.html", context)

""" Vendedores """

""" Vendedores - add """
def v_add(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del vendedor
        v_rut = request.POST["rut"]
        v_nombres = request.POST["nombres"]
        v_paterno = request.POST["paterno"]
        v_materno = request.POST["materno"]
        v_telefono = request.POST["telefono"]
        v_direccion = request.POST["direccion"]
        v_correo = request.POST["correo"]
        v_contrasenia = request.POST["contrasenia"]
        v_contrasenia2 = request.POST["contrasenia-2"]

        # Se valida si un vendedor ya existe mediante su rut
        if not vendedor.objects.filter(run = v_rut).exists():
            # Se valida que el correo que se esta intentando registrar no exista
            if not vendedor.objects.filter(correo = v_correo).exists():
                # Se valida si las contrasenias son iguales
                if (v_contrasenia == v_contrasenia2):
                    # Si son iguales se crea el objeto y se manda a la BD
                    obj = vendedor.objects.create(
                        run = v_rut,
                        nombres = v_nombres,
                        apaterno = v_paterno,
                        amaterno = v_materno,
                        direccion = v_direccion,
                        telefono = v_telefono,
                        correo = v_correo,
                        contrasenia = v_contrasenia,
                    )

                    obj.save()

                    # Se manda un mensaje de registro exitoso al usuario
                    print("Se registro")
                    context = {
                        "mensaje": "Registro exitoso!"
                    }
                    return render(request, "pages/crud/vendedores/v_add.html", context)
                else:
                    # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                    print("Contraseñas no coinciden")
                    context = {
                        "mensaje": "Las contraseñas no coinciden."
                    }
                    return render(request, "pages/crud/vendedores/v_add.html", context)
            else:
                # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                print("Correo ya registrado")
                context = {
                    "mensaje": "El correo ingresado ya esta registrado. Intente nuevamente."
                }
                return render(request, "pages/crud/vendedores/v_add.html", context)
        else:
            # En caso de que un vendedor ya exista se le manda un mensaje al usuario
            print("Vendedor ya registrado")
            context = {
            "mensaje": "Vendedor ingresado ya existe. Intente nuevamente."
            }
            return render(request, "pages/crud/vendedores/v_add.html", context)
    else:
        # Si el metodo no es POST
        context = {
            
        }
        return render(request, "pages/crud/vendedores/v_add.html", context)

""" Se busca el vendedor """
def v_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca al vendedor
        v_econtrado = vendedor.objects.get(run = pk)

        # Se le pasan los datos del vendedor encontrado al usuario en la vista de update
        context = {
            "vendedor": v_econtrado
        }
        return render(request, "pages/crud/vendedores/v_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra el vendedor buscado"
        }
        return render(request, "pages/crud/crud.html", context)

""" Vendedores - update """
def v_upd(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del vendedor
        v_rut = request.POST["rut"]
        v_nombres = request.POST["nombres"]
        v_paterno = request.POST["paterno"]
        v_materno = request.POST["materno"]
        v_telefono = request.POST["telefono"]
        v_direccion = request.POST["direccion"]
        v_correo = request.POST["correo"]
        v_contrasenia = request.POST["contrasenia"]
        v_contrasenia2 = request.POST["contrasenia-2"]

        # Se genera la instancia
        obj = vendedor(
            run = v_rut,
            nombres = v_nombres,
            apaterno = v_paterno,
            amaterno = v_materno,
            direccion = v_direccion,
            telefono = v_telefono,
            correo = v_correo,
            contrasenia = v_contrasenia,
        )

        # Se valida si las contrasenias son iguales
        if (v_contrasenia == v_contrasenia2):
            # Si son iguales se crea el objeto y se manda a la BD
            obj.save()

            # Se manda un mensaje de registro exitoso al usuario
            print("Se modifico")
            context = {
                "vendedor": obj,
                "mensaje": "Modificacion exitosa!"
            }
            return render(request, "pages/crud/vendedores/v_upd.html", context)
        else:
            # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
            print("Contraseñas no coinciden")
            context = {
                "vendedor": obj,
                "mensaje": "Las contraseñas no coinciden."
            }
            return render(request, "pages/crud/vendedores/v_upd.html", context)

""" Vendedores - delete """
def v_del(request, pk):
    try:
        # Se elimina el vendedor asociado a la pk
        v_encontrado = vendedor.objects.get(run = pk)
        v_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan 
        vendedores = vendedor.objects.all();
        clientes = cliente.objects.all();
        tarjetas = tarjeta.objects.all();
        pedidos = pedido.objects.all();
        detallePedidos = detallePedido.objects.all();
        productos = producto.objects.all();
        tipoProductos = tipoProducto.objects.all();

        context = {
            "vendedores": vendedores,
            "clientes": clientes,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Vendedor eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        vendedores = vendedor.objects.all();
        clientes = cliente.objects.all();
        tarjetas = tarjeta.objects.all();
        pedidos = pedido.objects.all();
        detallePedidos = detallePedido.objects.all();
        productos = producto.objects.all();
        tipoProductos = tipoProducto.objects.all();
        
        context = {
            "vendedores": vendedores,
            "clientes": clientes,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el vendedor")
        return render(request, "pages/crud/crud.html", context)
    
""" Clientes """

""" Clientes - add """
def c_add(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del cliente
        v_rut = request.POST["rut"]
        v_nombres = request.POST["nombres"]
        v_paterno = request.POST["paterno"]
        v_materno = request.POST["materno"]
        v_telefono = request.POST["telefono"]
        v_direccion = request.POST["direccion"]
        v_correo = request.POST["correo"]
        v_contrasenia = request.POST["contrasenia"]
        v_contrasenia2 = request.POST["contrasenia-2"]

        # Se valida si un cliente ya existe mediante su rut
        if not cliente.objects.filter(run = v_rut).exists():
            # Se valida que el correo que se esta intentando registrar no exista
            if not cliente.objects.filter(correo = v_correo).exists():
                # Se valida si las contrasenias son iguales
                if (v_contrasenia == v_contrasenia2):
                    # Si son iguales se crea el objeto y se manda a la BD
                    obj = cliente.objects.create(
                        run = v_rut,
                        nombres = v_nombres,
                        apaterno = v_paterno,
                        amaterno = v_materno,
                        direccion = v_direccion,
                        telefono = v_telefono,
                        correo = v_correo,
                        contrasenia = v_contrasenia,
                    )

                    obj.save()

                    # Se manda un mensaje de registro exitoso al usuario
                    print("Se registro")
                    context = {
                        "mensaje": "Registro exitoso!"
                    }
                    return render(request, "pages/crud/clientes/c_add.html", context)
                else:
                    # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                    print("Contraseñas no coinciden")
                    context = {
                        "mensaje": "Las contraseñas no coinciden."
                    }
                    return render(request, "pages/crud/clientes/c_add.html", context)
            else:
                # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                print("Correo ya registrado")
                context = {
                    "mensaje": "El correo ingresado ya esta registrado. Intente nuevamente."
                }
                return render(request, "pages/crud/clientes/c_add.html", context)
        else:
            # En caso de que un cliente ya exista se le manda un mensaje al usuario
            print("Cliente ya registrado")
            context = {
            "mensaje": "Cliente ingresado ya existe. Intente nuevamente."
            }
            return render(request, "pages/crud/clientes/c_add.html", context)
    else:
        # Si el metodo no es POST
        context = {
            
        }
        return render(request, "pages/crud/clientes/c_add.html", context)

""" Se busca al cliente """
def c_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca al cliente
        c_econtrado = cliente.objects.get(run = pk)

        # Se le pasan los datos del cliente encontrado al usuario en la vista de update
        context = {
            "cliente": c_econtrado
        }
        return render(request, "pages/crud/clientes/c_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra el cliente buscado"
        }
        return render(request, "pages/crud/clientes/c_upd.html", context)

""" Clientes - update """
def c_upd(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del vendedor
        c_rut = request.POST["rut"]
        c_nombres = request.POST["nombres"]
        c_paterno = request.POST["paterno"]
        c_materno = request.POST["materno"]
        c_telefono = request.POST["telefono"]
        c_direccion = request.POST["direccion"]
        c_correo = request.POST["correo"]
        c_contrasenia = request.POST["contrasenia"]
        c_contrasenia2 = request.POST["contrasenia-2"]

        # Se genera la instancia
        obj = cliente(
            run = c_rut,
            nombres = c_nombres,
            apaterno = c_paterno,
            amaterno = c_materno,
            direccion = c_direccion,
            telefono = c_telefono,
            correo = c_correo,
            contrasenia = c_contrasenia,
        )

        # Se valida si las contrasenias son iguales
        if (c_contrasenia == c_contrasenia2):
            # Si son iguales se crea el objeto y se manda a la BD
            obj.save()

            # Se manda un mensaje de registro exitoso al usuario
            print("Se modifico")
            context = {
                "cliente": obj,
                "mensaje": "Modificacion exitosa!"
            }
            return render(request, "pages/crud/clientes/c_upd.html", context)
        else:
            # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
            print("Contraseñas no coinciden")
            context = {
                "cliente": obj,
                "mensaje": "Las contraseñas no coinciden."
            }
            return render(request, "pages/crud/clientes/c_upd.html", context)
""" Clientes - delete """
def c_del(request, pk):
    try:
        # Se elimina el cliente asociado a la pk
        c_encontrado = cliente.objects.get(run = pk)
        c_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Cliente eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el cliente")
        return render(request, "pages/crud/crud.html", context)

""" Tarjetas de clientes """

""" Tarjetas de clientes - add """
def tc_add(request):
    # Se mandan los clientes para el select
    if request.method != "POST":
        context = {
            "clientes": cliente.objects.all()
        }
        return render(request, "pages/crud/tarjetas/tc_add.html", context)
    else:
        # Datos de la tarjeta
        tar = request.POST["tarjeta"]
        cli = request.POST["cliente"]

        # Se recupera el run del cliente
        objCli = cliente.objects.get(run = cli)

        # Se crea el objeto y se manda a la BD
        obj = tarjeta.objects.create(
            nro_tarjeta = tar,
            cliente = objCli
        )

        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "mensaje": "Registro exitoso!"
        }
        return render(request, "pages/crud/tarjetas/tc_add.html", context)

""" Se busca la tarjeta del cliente """
def tc_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca la tarjeta y se traen todos los clientes
        tar = tarjeta.objects.get(nro_tarjeta = pk)
        clientes = cliente.objects.all()

        context = {
            "tarjeta" : tar,
            "clientes" : clientes
        }
        return render(request, "pages/crud/tarjetas/tc_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra la tarjeta buscada"
        }
        return render(request, "pages/crud/tarjetas/tc_upd.html", context)

""" Tarjetas de clientes - update """
def tc_upd(request):
    if request.method == "POST":
        # Datos de la tarjeta
        tar = request.POST["tarjeta"]
        cli = request.POST["cliente"]

        # Se recupera el run del cliente
        objCli = cliente.objects.get(run = cli)

        # Se crea el objeto y se manda a la BD
        obj = tarjeta(
            nro_tarjeta = tar,
            cliente = objCli
        )

        obj.save()

        # Se manda un mensaje de modificacion exitosa al usuario
        clientes = cliente.objects.all()
        context = {
            "mensaje": "Modificación exitosa!",
            "tarjeta": obj,
            "clientes": clientes
        }
        return render(request, "pages/crud/tarjetas/tc_upd.html", context)

""" Tarjetas de cliente - delete """
def tc_del(request, pk):
    try:
        tc_encontrada = tarjeta.objects.get(nro_tarjeta = pk)
        tc_encontrada.delete()

        # Se recuperan los datos de la BD y se mandan 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Tarjeta eliminada")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar la tarjeta")
        return render(request, "pages/crud/crud.html", context)

""" Pedidos """
def p_add(request):
    context = {
        
    }
    return render(request, "pages/crud/pedidos/p_add.html", context)

""" Pedidos - add"""

""" Detalle de pedidos """

""" Productos """

""" Tipos de productos """

