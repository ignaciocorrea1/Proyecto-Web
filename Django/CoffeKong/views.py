from django.shortcuts import render, redirect
from .models import cliente, vendedor, tarjeta, estado, pedido, tipoProducto, producto, detallePedido
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

""" Credenciales para pruebas: 
    - Vendedor: 
        testv@gmail.com
        testven1
    - Cliente:
        testc@gmail.com  
        testcli1

    * El vendedor no podrá ver su tabla en el crud, solo el admin.
"""

""" Decorador para saber el grupo al que pertenece el usuario """
def check_group(group1, group2):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group1).exists() or request.user.groups.filter(name=group2).exists() :
                return function(request, *args, **kwargs)
            return redirect('login')
        return wrapper
    return decorator

""" Función para importar los productos del Json a la BD
def import_data():
    try:
        # Se leen los datos
        with open('CoffeKong/static/json/productos.json', 'r', encoding='utf-8') as json_file:
            # Se crea y se asigna un diccionario a "productos"
            productos = json.load(json_file)
            print(productos)

            # Se recorren los datos para crear los "productos"
            for p in productos:
                # Se generan instancias del tipo de producto para poder agregar mi producto
                objTipo = tipoProducto.objects.get(id_tipoproducto = p["tipo"])
                print(p["tipo"])

                # Se crea un objeto y se manda a la BD
                p = producto.objects.create(
                    id_producto = p["id"],
                    nombre = p["nombre"],
                    descripcion = p["descripcion"],
                    precio = p["precio"],
                    imagen = p["imagen"],
                    tipo = objTipo
                )
                print("Producto creado")
                p.save()
            
            productos.close()
                
    except Exception as e:
        print("Error al cargar el Json", e) """

def index(request):
    context = {}
    # import_data()
    return render(request, "pages/index.html", context)

def menu(request):
    productos = producto.objects.all()
    context = {
        "productos": productos,
    }
    return render(request, "pages/menu.html", context)

def unete(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del cliente
        c_rut = request.POST["rut"]
        c_nombres = request.POST["nombres"]
        c_paterno = request.POST["paterno"]
        c_materno = request.POST["materno"]
        c_telefono = request.POST["telefono"]
        c_direccion = request.POST["direccion"]
        c_correo = request.POST["correo"]
        c_contrasenia = request.POST["contrasenia"]
        c_contrasenia2 = request.POST["contrasenia-2"]

        # Se valida si un cliente ya existe mediante su rut
        if not cliente.objects.filter(run = c_rut).exists():
            # Se valida que el correo que se esta intentando registrar no exista
            if not cliente.objects.filter(correo = c_correo).exists():
                # Se valida si las contrasenias son iguales
                if (c_contrasenia == c_contrasenia2):
                    # Si son iguales se crea el objeto y se manda a la BD
                    obj = cliente.objects.create(
                        run = c_rut,
                        nombres = c_nombres,
                        apaterno = c_paterno,
                        amaterno = c_materno,
                        direccion = c_direccion,
                        telefono = c_telefono,
                        correo = c_correo,
                        contrasenia = c_contrasenia,
                    )

                    obj.save()
                    
                    c_apellido = c_paterno+" "+c_materno

                    # Se crea un usuario en el modelo de Users
                    user = User.objects.create_user(
                        username = c_correo,
                        password = c_contrasenia,
                        first_name = c_nombres,
                        last_name = c_apellido,
                        email = c_correo
                    )
                    
                    # Se obtiene el grupo del cliente
                    cliente_group = Group.objects.get(name="cliente_group")

                    # Se le asigna el grupo al usuario y despues se guarda
                    user.groups.add(cliente_group)
                    user.save()

                    # Se manda un mensaje de registro exitoso al usuario
                    context = {
                        "mensaje": "Registro exitoso!",
                        "design": "alert alert-success w-50 mx-auto text-center"
                    }
                    return render(request, "pages/unete.html", context)
                else:
                    # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                    context = {
                        "mensaje": "Las contraseñas no coinciden.",
                        "design": "alert alert-danger w-50 mx-auto text-center"
                    }
                    return render(request, "pages/unete.html", context)
            else:
                # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                context = {
                    "mensaje": "El correo ingresado ya esta registrado. Intente nuevamente.",
                    "design": "alert alert-danger w-50 mx-auto text-center"
                }
                return render(request, "pages/unete.html", context)
        else:
            # En caso de que un cliente ya exista se le manda un mensaje al usuario
            context = {
                "mensaje": "Rut ingresado ya se encuentra registrado. Intente nuevamente.",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/unete.html", context)
    else:
        # Si el metodo no es POST
        context = {
            
        }
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

def contrasenia(request):
    context = {}
    return render(request, "pages/contrasenia.html", context)

def historial(request):
    context = {}
    return render(request, "pages/historial.html", context)

def detalle(request):
    context = {}
    return render(request, "pages/detalle.html", context)
        
""" Login """
def conectar(request):
    # Si el usuario no esta logeado puede logearse, sino los campos estarán en readonly
    if not request.user.is_authenticated:
        # Si el metodo es POST
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            usuario = authenticate(request, username=username, password=password)

            if usuario is not None:
                login(request, usuario)
            
                # Se valida el tipo de usuario
                if vendedor.objects.filter(correo = username).exists():
                    request.session["tipo_usuario"] = "vendedor"
                elif cliente.objects.filter(correo = username).exists():
                    request.session["tipo_usuario"] = "cliente"
                else:
                    request.session["tipo_usuario"] = "admin"

                context = {
                    
                }
                return render(request, "pages/index.html", context)
            else:
                context = {
                    "mensaje": "Usuario o contraseña incorrecta.",
                    "design": "alert alert-danger w-50 mx-auto text-center"
                }
                return render(request, "pages/ingreso.html", context)
        else:
            context = {
                "estado": ""
            }
            return render(request, "pages/ingreso.html", context)
    else:
        context = {
            "mensaje": "Ya se encuentra logeado",
            "design": "alert alert-info w-50 mx-auto text-center",
            "estado": "readonly",
        }
        return render(request, "pages/ingreso.html", context)

    
def desconectar(request):
    if request.user.is_authenticated:
        logout(request)
    
    context = {

    }
    return render(request,"pages/ingreso.html",context)

""" Crud """
@login_required
@check_group("vendedor_group", "admin_group")
def crud(request):
    vendedores = vendedor.objects.all()
    clientes = cliente.objects.all()
    tarjetas = tarjeta.objects.all()
    estados = estado.objects.all()
    pedidos = pedido.objects.all()
    detallePedidos = detallePedido.objects.all()
    productos = producto.objects.all()
    tipoProductos = tipoProducto.objects.all()

    context = {
        "vendedores": vendedores,
        "clientes": clientes,
        "tarjetas": tarjetas,
        "estados": estados,
        "pedidos": pedidos,
        "detallePedidos": detallePedidos,
        "productos": productos,
        "tipoProductos": tipoProductos,
    }
    return render(request, "pages/crud/crud.html", context)

""" Vendedores """

""" Vendedores - add """
@login_required
@check_group("vendedor_group", "admin_group")
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
                    
                    v_apellido = v_paterno+" "+v_materno

                    # Se crea un usuario en el modelo de Users
                    user = User.objects.create_user(
                        username = v_correo,
                        password = v_contrasenia,
                        first_name = v_nombres,
                        last_name = v_apellido,
                        email = v_correo
                    )
                    
                    # Se obtiene el grupo del vendedor
                    vendedor_group = Group.objects.get(name="vendedor_group")

                    # Se le asigna el grupo al usuario y despues se guarda
                    user.groups.add(vendedor_group)
                    user.save()
                    
                    # Se manda un mensaje de registro exitoso al usuario
                    print("Se registro")
                    context = {
                        "mensaje": "Registro exitoso!",
                        "design": "alert alert-success w-50 mx-auto text-center"
                    }
                    return render(request, "pages/crud/vendedores/v_add.html", context)
                else:
                    # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                    print("Contraseñas no coinciden")
                    context = {
                        "mensaje": "Las contraseñas no coinciden.",
                        "design": "alert alert-danger w-50 mx-auto text-center"
                    }
                    return render(request, "pages/crud/vendedores/v_add.html", context)
            else:
                # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                print("Correo ya registrado")
                context = {
                    "mensaje": "El correo ingresado ya esta registrado. Intente nuevamente.",
                    "design": "alert alert-danger w-50 mx-auto text-center"
                }
                return render(request, "pages/crud/vendedores/v_add.html", context)
        else:
            # En caso de que un vendedor ya exista se le manda un mensaje al usuario
            print("Vendedor ya registrado")
            context = {
                "mensaje": "Vendedor ingresado ya existe. Intente nuevamente.",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/vendedores/v_add.html", context)
    else:
        # Si el metodo no es POST
        context = {
            
        }
        return render(request, "pages/crud/vendedores/v_add.html", context)

""" Se busca el vendedor """
@login_required
@check_group("vendedor_group", "admin_group")
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
@login_required
@check_group("vendedor_group", "admin_group")
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

            v_apellido = v_paterno+" "+v_materno

            # Se modifica el usuario
            user = User.objects.get(email = v_correo)

            user.first_name = v_nombres
            user.last_name = v_apellido
            user.set_password(v_contrasenia)

            user.save()
            print(v_contrasenia)
            # Se manda un mensaje de registro exitoso al usuario
            print("Se modifico")
            context = {
                "vendedor": obj,
                "mensaje": "Modificacion exitosa!",
                "design": "alert alert-success w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/vendedores/v_upd.html", context)
        else:
            # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
            print("Contraseñas no coinciden")
            context = {
                "vendedor": obj,
                "mensaje": "Las contraseñas no coinciden.",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/vendedores/v_upd.html", context)

""" Vendedores - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def v_del(request, pk):
    try:
        # Se elimina el vendedor y su usuario asociado a la pk
        v_encontrado = vendedor.objects.get(run = pk)
        user = User.objects.get(email = v_encontrado.correo)
        v_encontrado.delete()
        user.delete()

        # Se recuperan los datos de la BD y se mandan 
        vendedores = vendedor.objects.all()
        clientes = cliente.objects.all()
        tarjetas = tarjeta.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "vendedores": vendedores,
            "clientes": clientes,
            "tarjetas": tarjetas,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Vendedor eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        vendedores = vendedor.objects.all()
        clientes = cliente.objects.all()
        tarjetas = tarjeta.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()
        
        context = {
            "vendedores": vendedores,
            "clientes": clientes,
            "tarjetas": tarjetas,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el vendedor")
        return render(request, "pages/crud/crud.html", context)
    
""" Clientes """

""" Clientes - add """
@login_required
@check_group("vendedor_group", "admin_group")
def c_add(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del cliente
        c_rut = request.POST["rut"]
        c_nombres = request.POST["nombres"]
        c_paterno = request.POST["paterno"]
        c_materno = request.POST["materno"]
        c_telefono = request.POST["telefono"]
        c_direccion = request.POST["direccion"]
        c_correo = request.POST["correo"]
        c_contrasenia = request.POST["contrasenia"]
        c_contrasenia2 = request.POST["contrasenia-2"]

        # Se valida si un cliente ya existe mediante su rut
        if not cliente.objects.filter(run = c_rut).exists():
            # Se valida que el correo que se esta intentando registrar no exista
            if not cliente.objects.filter(correo = c_correo).exists():
                # Se valida si las contrasenias son iguales
                if (c_contrasenia == c_contrasenia2):
                    # Si son iguales se crea el objeto y se manda a la BD
                    obj = cliente.objects.create(
                        run = c_rut,
                        nombres = c_nombres,
                        apaterno = c_paterno,
                        amaterno = c_materno,
                        direccion = c_direccion,
                        telefono = c_telefono,
                        correo = c_correo,
                        contrasenia = c_contrasenia,
                    )

                    obj.save()
                    
                    c_apellido = c_paterno+" "+c_materno

                    # Se crea un usuario en el modelo de Users
                    user = User.objects.create_user(
                        username = c_correo,
                        password = c_contrasenia,
                        first_name = c_nombres,
                        last_name = c_apellido,
                        email = c_correo
                    )
                    
                    # Se obtiene el grupo del cliente
                    cliente_group = Group.objects.get(name="cliente_group")

                    # Se le asigna el grupo al usuario y despues se guarda
                    user.groups.add(cliente_group)
                    user.save()

                    # Se manda un mensaje de registro exitoso al usuario
                    print("Se registro")
                    context = {
                        "mensaje": "Registro exitoso!",
                        "design": "alert alert-success w-50 mx-auto text-center"
                    }
                    return render(request, "pages/crud/clientes/c_add.html", context)
                else:
                    # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                    print("Contraseñas no coinciden")
                    context = {
                        "mensaje": "Las contraseñas no coinciden.",
                        "design": "alert alert-danger w-50 mx-auto text-center"
                    }
                    return render(request, "pages/crud/clientes/c_add.html", context)
            else:
                # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
                print("Correo ya registrado")
                context = {
                    "mensaje": "El correo ingresado ya esta registrado. Intente nuevamente.",
                    "design": "alert alert-danger w-50 mx-auto text-center"
                }
                return render(request, "pages/crud/clientes/c_add.html", context)
        else:
            # En caso de que un cliente ya exista se le manda un mensaje al usuario
            print("Cliente ya registrado")
            context = {
                "mensaje": "Cliente ingresado ya existe. Intente nuevamente.",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/clientes/c_add.html", context)
    else:
        # Si el metodo no es POST
        context = {
            
        }
        return render(request, "pages/crud/clientes/c_add.html", context)

""" Se busca al cliente """
@login_required
@check_group("vendedor_group", "admin_group")
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
@login_required
@check_group("vendedor_group", "admin_group")
def c_upd(request):
    # Si el metodo es POST
    if request.method == "POST":

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

            c_apellido = c_paterno+" "+c_materno

            # Se modifica el usuario
            user = User.objects.get(email = c_correo)

            user.first_name = c_nombres
            user.last_name = c_apellido
            user.set_password(c_contrasenia)

            user.save()

            # Se manda un mensaje de registro exitoso al usuario
            print("Se modifico")
            context = {
                "cliente": obj,
                "mensaje": "Modificacion exitosa!",
                "design": "alert alert-success w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/clientes/c_upd.html", context)
        else:
            # En caso de que las contrasenias no son iguales se le manda un mensaje al usuario
            print("Contraseñas no coinciden")
            context = {
                "cliente": obj,
                "mensaje": "Las contraseñas no coinciden.",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/clientes/c_upd.html", context)

""" Clientes - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def c_del(request, pk):
    try:
        # Se elimina el cliente y su usuario asociado a la pk
        c_encontrado = cliente.objects.get(run = pk)
        user = User.objects.get(email = c_encontrado.correo)
        c_encontrado.delete()
        user.delete()

        # Se recuperan los datos de la BD y se mandan 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "estados": estados,
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
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el cliente")
        return render(request, "pages/crud/crud.html", context)

""" Tarjetas de clientes """

""" Tarjetas de clientes - add """
@login_required
@check_group("vendedor_group", "admin_group")
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

        # Se recupera el cliente
        objCli = cliente.objects.get(run = cli)

        # Se crea el objeto y se manda a la BD
        obj = tarjeta.objects.create(
            nro_tarjeta = tar,
            cliente = objCli
        )

        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "mensaje": "Registro exitoso!",
            "design": "alert alert-success w-50 mx-auto text-center"
        }
        return render(request, "pages/crud/tarjetas/tc_add.html", context)

""" Se busca la tarjeta del cliente """
@login_required
@check_group("vendedor_group", "admin_group")
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
@login_required
@check_group("vendedor_group", "admin_group")
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
            "design": "alert alert-success w-50 mx-auto text-center",
            "tarjeta": obj,
            "clientes": clientes
        }
        return render(request, "pages/crud/tarjetas/tc_upd.html", context)

""" Tarjetas de cliente - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def tc_del(request, pk):
    try:
        tc_encontrada = tarjeta.objects.get(nro_tarjeta = pk)
        tc_encontrada.delete()

        # Se recuperan los datos de la BD y se mandan 
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Tarjeta eliminada")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar la tarjeta")
        return render(request, "pages/crud/crud.html", context)

""" Estados de pedido """

""" Estados de pedido - add """
@login_required
@check_group("vendedor_group", "admin_group")
def e_add(request):
    if request.method == "POST":
        # Si el metodo es POST

        # Datos del estado
        e_estado = request.POST["estado"]

        # Se crea un objeto y se manda a la BD
        # Al ser la id autonumerica se menciona solo la descripcion
        obj = estado.objects.create(descripcion = e_estado)
        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "mensaje": "Registro exitoso!",
            "design": "alert alert-success w-50 mx-auto text-center"        
        }
        return render(request, "pages/crud/estados/e_add.html", context)
    else:
        context = {
            
        }
        return render(request, "pages/crud/estados/e_add.html", context)
    
""" Se busca un estado de pedido """
@login_required
@check_group("vendedor_group", "admin_group")
def e_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca el estado y se mandan los datos
        e_encontrado = estado.objects.get(id_estado = pk)

        # Se pasan los datos encontrados al usuario
        context = {
            "estado": e_encontrado,
        }
        return render(request, "pages/crud/estados/e_upd.html", context)
    else:
        context = {

        }
        return render(request, "pages/crud/estados/e_upd.html", context)

""" Estados de pedido - update """
@login_required
@check_group("vendedor_group", "admin_group")
def e_upd(request):
    # Si el metodo es POST
    if request.method == "POST":

        # Datos del estado
        e_id = request.POST["id_estado"]
        e_estado = request.POST["estado"]

        # Se modifica el objeto y se manda a la BD
        obj = estado(
            id_estado = e_id,
            descripcion = e_estado
            )
        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "estado": obj,
            "mensaje": "Modificación exitosa!",
            "design": "alert alert-success w-50 mx-auto text-center"        
        }
        return render(request, "pages/crud/estados/e_upd.html", context)
    else:
        context = {
            
        }
        return render(request, "pages/crud/estados/e_upd.html", context)

""" Estados de pedido - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def e_del(request, pk):
    try:
        # Se elimina el estado de pedido asociado a la pk
        e_encontrado = estado.objects.get(id_estado = pk)
        e_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan
        estados = estado.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "estados": estados,
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Estado de pedido eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan
        estados = estado.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()
    
        context = {
            "estados": estados,
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el estado de pedido")
        return render(request, "pages/crud/crud.html", context)

""" Pedidos """

""" Pedidos - add"""
@login_required
@check_group("vendedor_group", "admin_group")
def p_add(request):
    if request.method == "POST":
        # Datos del pedido
        p_fecha = request.POST["fecha"]
        p_cliente = request.POST["cliente"]
        p_estado = request.POST["estado"]

        # Se recupera el cliente y el estado
        objCli = cliente.objects.get(run = p_cliente)
        objEst = estado.objects.get(id_estado = p_estado)

        # Se crea el objeto y se manda a la BD
        obj = pedido.objects.create(
            cliente = objCli,
            fecha = p_fecha,
            estado = objEst
        )
        obj.save()

        # Se manda un mensaje de confirmacion al usuario
        context = {
            "mensaje": "Registro exitoso!",
            "design": "alert alert-success w-50 mx-auto text-center"
        }
        print("Se registro")
        return render(request, "pages/crud/pedidos/p_add.html", context)
    else:
        # Se mandan los clientes y estados al usuario
        clientes = cliente.objects.all()
        estados = estado.objects.all()
        context = {
            "clientes": clientes,
            "estados": estados
        }
        print("No se registro")
        return render(request, "pages/crud/pedidos/p_add.html", context)

""" Se busca el pedido """
@login_required
@check_group("vendedor_group", "admin_group")
def p_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca el pedido y se traen los clientes y estados asociados
        ped = pedido.objects.get(id_pedido = pk)
        clientes = cliente.objects.all()
        estados = estado.objects.all()

        context = {
            "pedido": ped,
            "clientes": clientes,
            "estados": estados
        }
        return render(request, "pages/crud/pedidos/p_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra el pedido buscado"
        }
        return render(request, "pages/crud/pedidos/p_upd.html", context)

""" Pedidos - update """
@login_required
@check_group("vendedor_group", "admin_group")
def p_upd(request):
    # Si el metodo es POST
    if request.method == "POST":

        # Datos del pedido
        p_id = request.POST["id_pedido"]
        p_fecha = request.POST["fecha"]
        p_cliente = request.POST["cliente"]
        p_estado = request.POST["estado"]

        # Se recupera el cliente y el estado
        objCli = cliente.objects.get(run = p_cliente)
        objEst = estado.objects.get(id_estado = p_estado)

        # Se crea el objeto y se manda a la BD
        obj = pedido(
            id_pedido = p_id,
            cliente = objCli,
            fecha = p_fecha,
            estado = objEst
        )
        obj.save()

        # Se mandan los datos del pedido, clientes y estados al usuario
        # EL pedido se manda de esta forma porque al intentarlo con "obj" la fecha se formateaba
        ped = pedido.objects.get(id_pedido = p_id)
        clientes = cliente.objects.all()
        estados = estado.objects.all()
        context = {
            "mensaje": "Modificación exitosa!",
            "design": "alert alert-success w-50 mx-auto text-center",
            "pedido": ped,
            "clientes": clientes,
            "estados": estados
        }
        return render(request, "pages/crud/pedidos/p_upd.html", context)

""" Pedidos - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def p_del(request, pk):
    try:
        p_encontrado = pedido.objects.get(id_pedido = pk)
        p_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan 
        pedidos = pedido.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        estados = estado.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "pedidos": pedidos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print("Pedido eliminado")
        return render(request, "pages/crud/crud.html", context)
    except Exception as e:
        # Se recuperan los datos de la BD y se mandan
        pedidos = pedido.objects.all() 
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        estados = estado.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "pedidos": pedidos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tipoProductos": tipoProductos,
        }
        print(e)
        return render(request, "pages/crud/crud.html", context)
    
""" Detalle de pedidos """

""" Detalle de pedidos - add """
@login_required
@check_group("vendedor_group", "admin_group")
def dt_add(request):
    # Si el metodo es POST
    if request.method == "POST":

        # Datos del detalle
        dt_pedido = request.POST["pedido"]
        dt_producto = request.POST["producto"]
        dt_total = request.POST["total"]
        dt_cantidad = request.POST["cantidad"]

        objPed = pedido.objects.get(id_pedido = dt_pedido)
        objPro = producto.objects.get(id_producto = dt_producto)

        # Se crea el objeto y se manda a la BD
        obj = detallePedido.objects.create(
            id_pedido = objPed,
            id_producto = objPro,
            total = dt_total,
            cantidad = dt_cantidad
        )
        obj.save()
        
        pedidos = pedido.objects.all()
        productos = producto.objects.all()
        context = {
            "mensaje": "Registro exitoso!",
            "design": "alert alert-success w-50 mx-auto text-center",
            "pedidos": pedidos,
            "productos": productos
        }
        return render(request, "pages/crud/detalle/dt_add.html", context)
    else:
        pedidos = pedido.objects.all()
        productos = producto.objects.all()
        context = {
            "pedidos": pedidos,
            "productos": productos
        }
        return render(request, "pages/crud/detalle/dt_add.html", context)

""" Se busca un detalle de pedido """
@login_required
@check_group("vendedor_group", "admin_group")
def dt_find(request, pk):
    if pk != "":
        # Si las pks no estan vacias se busca el detalle asociado, mas todos los pedidos y productos para el select
        detalles = detallePedido.objects.get(id_pedido = pk)
        pedidos = pedido.objects.all()
        productos = producto.objects.all()

        context = {
            "detalle": detalles,
            "pedidos": pedidos,
            "productos": productos
        }
        return render(request, "pages/crud/detalle/dt_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra el detalle de pedido buscado"

        }
        return render(request, "pages/crud/detalle/dt_upd.html", context)

""" Detalle de pedidos - update """
@login_required
@check_group("vendedor_group", "admin_group")
def dt_upd(request):
    # Si el metodo es POST
    if request.method == "POST":

        # Datos del detalle
        dt_id = request.POST["id_detalle"]
        dt_pedido = request.POST["pedido"]
        dt_producto = request.POST["producto"]
        dt_total = request.POST["total"]
        dt_cantidad = request.POST["cantidad"]

        objPed = pedido.objects.get(id_pedido = dt_pedido)
        objPro = producto.objects.get(id_producto = dt_producto)

        # Se crea el objeto y se manda a la BD
        obj = detallePedido(
            id_detalle = dt_id,
            id_pedido = objPed,
            id_producto = objPro,
            total = dt_total,
            cantidad = dt_cantidad
        )
        obj.save()
        
        pedidos = pedido.objects.all()
        productos = producto.objects.all()
        context = {
            "mensaje": "Modificación exitosa!",
            "design": "alert alert-success w-50 mx-auto text-center",
            "detalle": obj,
            "pedidos": pedidos,
            "productos": productos
        }
        return render(request, "pages/crud/detalle/dt_upd.html", context)
    
""" Detalle de pedidos - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def dt_del(request, pk):
    try:
        det = detallePedido.objects.get(id_pedido = pk)
        det.delete()

        # Se recuperan los datos de la BD y se mandan 
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "tipoProductos": tipoProductos,
        }
        print("Detalle eliminado")
        return render(request, "pages/crud/crud.html", context)
    except Exception as e:
        # Se recuperan los datos de la BD y se mandan 
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "detallePedidos": detallePedidos,
            "productos": productos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "tipoProductos": tipoProductos,
        }
        print(e)
        return render(request, "pages/crud/crud.html", context)

""" Productos """

""" Productos - add """
@login_required
@check_group("vendedor_group", "admin_group")
def pr_add(request):
    # Si el metodo es POST
    if request.method == "POST":

        # Datos del producto
        pr_id = request.POST["id"]
        pr_nombre = request.POST["nombre"]
        pr_desc = request.POST["descripcionp"]
        pr_precio = request.POST["precio"]
        pr_imagen = request.POST["imagen"]
        pr_tipo = request.POST["tipo"]

        # Si valida que la id ingresada no exista
        if not producto.objects.filter(id_producto = pr_id).exists():
            objTipo = tipoProducto.objects.get(id_tipoproducto = pr_tipo)

            # Se crea el objeto y se manda a la BD
            obj = producto.objects.create(
                id_producto = pr_id,
                nombre = pr_nombre,
                descripcion = pr_desc,
                precio = pr_precio,
                imagen = pr_imagen,
                tipo = objTipo
            )
            obj.save()

            # Se manda un mensaje de registro exitoso al usuario
            context = {
                "mensaje": "Registro exitoso!",
                "design": "alert alert-success w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/productos/pr_add.html", context)
        else:
            # Se mandan los tipos de producto al usuario
            tipos = tipoProducto.objects.all()
            context = {
                "tipoProductos": tipos, 
                "mensaje": "La id ingresada ya se encuentra registrada. Intente nuevamente",
                "design": "alert alert-danger w-50 mx-auto text-center"
            }
            return render(request, "pages/crud/productos/pr_add.html", context)

    else:
        # Se mandan los tipos de producto al usuario
        tipos = tipoProducto.objects.all()
        context = {
            "tipoProductos": tipos,
        }
        return render(request, "pages/crud/productos/pr_add.html", context)

""" Se busca el producto """
@login_required
@check_group("vendedor_group", "admin_group")
def pr_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca el producto y se traen los tipos de productos
        prod = producto.objects.get(id_producto = pk)
        tipos = tipoProducto.objects.all()

        context = {
            "producto": prod,
            "tipoProductos": tipos
        }
        return render(request, "pages/crud/productos/pr_upd.html", context)
    else:
        context = {
            "mensaje": "No se encuentra el producto buscado"
        }
        return render(request, "pages/crud/productos/pr_upd.html", context)
    
""" Productos - update """
@login_required
@check_group("vendedor_group", "admin_group")
def pr_upd(request):
    if request.method == "POST":

        # Datos del producto
        pr_id = request.POST["id"]
        pr_nombre = request.POST["nombre"]
        pr_desc = request.POST["descripcionp"]
        pr_precio = request.POST["precio"]
        pr_imagen = request.POST["imagen"]
        pr_tipo = request.POST["tipo"]

        objTipo = tipoProducto.objects.get(id_tipoproducto = pr_tipo)

        # Se crea el objeto y se manda a la BD
        obj = producto(
            id_producto = pr_id,
            nombre = pr_nombre,
            descripcion = pr_desc,
            precio = pr_precio,
            imagen = pr_imagen,
            tipo = objTipo
        )
        obj.save()

        # Se manda un mensaje de modificacion exitosa al usuario 
        tipos = tipoProducto.objects.all()
        context = {
            "mensaje": "Modificación exitosa!",
            "design": "alert alert-success w-50 mx-auto text-center",
            "producto": obj,
            "tipoProductos": tipos
        }
        return render(request, "pages/crud/productos/pr_upd.html", context)

""" Productos - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def pr_del(request, pk):
    try:
        pr_encontrado = producto.objects.get(id_producto = pk)
        pr_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan 
        productos = producto.objects.all()
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "productos": productos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "tipoProductos": tipoProductos,
        }
        print("Producto eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan 
        productos = producto.objects.all()
        tarjetas = tarjeta.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        estados = estado.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "productos": productos,
            "tarjetas": tarjetas,
            "clientes": clientes,
            "vendedores": vendedores,
            "estados": estados,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "tipoProductos": tipoProductos,
        }
        print("No se pudo eliminar el producto")
        return render(request, "pages/crud/crud.html", context)


""" Tipos de productos """

""" Tipos de productos - add """
@login_required
@check_group("vendedor_group", "admin_group")
def tp_add(request):
    # Si el metodo es POST
    if request.method == "POST":
        # Datos del tipo de producto
        tp_id = request.POST["id"]
        tp_descripcion = request.POST["descripcion"]

        # Se crea un objeto y se manda a la BD
        obj = tipoProducto.objects.create(
            id_tipoproducto = tp_id,
            descripcion = tp_descripcion
        )
        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "mensaje": "Registro exitoso!",
            "design": "alert alert-success w-50 mx-auto text-center"
        }
        return render(request, "pages/crud/tipo_productos/tp_add.html", context)
    else:
        context = {
            
        }
        return render(request, "pages/crud/tipo_productos/tp_add.html", context)
    
""" Se busca el tipo de producto """
@login_required
@check_group("vendedor_group", "admin_group")
def tp_find(request, pk):
    if pk != "":
        # Si la pk no esta vacia se busca el tipo de producto y se mandan los datos
        tp_encontrado = tipoProducto.objects.get(id_tipoproducto = pk)

        context = {
            "tipo": tp_encontrado,
        }
        return render(request, "pages/crud/tipo_productos/tp_upd.html", context)
    else:
        context = {

        }
        return render(request, "pages/crud/tipo_productos/tp_upd.html", context)
    
""" Tipo de producto - update """
@login_required
@check_group("vendedor_group", "admin_group")
def tp_upd(request):
    # Si el metodo es POST
    if request.method == "POST":
        # Datos del tipo de producto
        tp_id = request.POST["id"]
        tp_descripcion = request.POST["descripcion"]

        # Se modifica el objeto y se manda a la BD
        obj = tipoProducto(
            id_tipoproducto = tp_id,
            descripcion = tp_descripcion
        )
        obj.save()

        # Se manda un mensaje de registro exitoso al usuario
        context = {
            "tipo": obj,
            "mensaje": "Modificación exitosa!",
            "design": "alert alert-success w-50 mx-auto text-center"
        }
        return render(request, "pages/crud/tipo_productos/tp_upd.html", context)
    
""" Tipo de producto - delete """
@login_required
@check_group("vendedor_group", "admin_group")
def tp_del(request, pk):
    try:
        tp_encontrado = tipoProducto.objects.get(id_tipoproducto = pk)
        tp_encontrado.delete()

        # Se recuperan los datos de la BD y se mandan
        estados = estado.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tipoProductos": tipoProductos,
            "estados": estados,
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
        }
        print("Tipo de producto eliminado")
        return render(request, "pages/crud/crud.html", context)
    except:
        # Se recuperan los datos de la BD y se mandan
        estados = estado.objects.all()
        clientes = cliente.objects.all()
        vendedores = vendedor.objects.all()
        tarjetas = tarjeta.objects.all()
        pedidos = pedido.objects.all()
        detallePedidos = detallePedido.objects.all()
        productos = producto.objects.all()
        tipoProductos = tipoProducto.objects.all()

        context = {
            "tipoProductos": tipoProductos,
            "estados": estados,
            "clientes": clientes,
            "vendedores": vendedores,
            "tarjetas": tarjetas,
            "pedidos": pedidos,
            "detallePedidos": detallePedidos,
            "productos": productos,
        }
        print("No se pudo eliminar el tipo de producto")
        return render(request, "pages/crud/crud.html", context)