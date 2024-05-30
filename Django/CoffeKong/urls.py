from django.urls import path
from CoffeKong import views

""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("unete", views.unete, name="unete"),
    path("seguimiento", views.seguimiento, name="seguimiento"),
    path("seguimiento2", views.seguimiento2, name="seguimiento2"),
    path("carrito", views.carrito, name="carrito"),
    path("pago", views.pago, name="pago"),
    path("ingreso", views.ingreso, name="ingreso"),
    path("contrasenia", views.contrasenia, name="contrasenia"),
    path("historial", views.historial, name="historial"),
    path("detalle", views.detalle, name="detalle"),
]