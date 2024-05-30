from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "pages/index.html", context)

def menu(request):
    context = {}
    return render(request, "pages/menu.html", context)

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
