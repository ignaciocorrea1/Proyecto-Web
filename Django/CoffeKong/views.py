from django.shortcuts import render
from .models import cliente, vendedor, tarjeta, tipoProducto, producto, pedido, detallePedido
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

def crud(request):
    # Vendedores
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
    return render(request, "pages/crud/crud.html", context)
