from django.urls import path
from CoffeKong import views

""" path('nombreURL',funcionVista,nombreDePagina) """
urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("unete/", views.unete, name="unete"),
    path("seguimiento/", views.seguimiento, name="seguimiento"),
    path("seguimiento2/", views.seguimiento2, name="seguimiento2"),
    path("carrito/", views.carrito, name="carrito"),
    path("pago/", views.pago, name="pago"),
    path("ingreso/", views.ingreso, name="ingreso"),
    path("contrasenia/", views.contrasenia, name="contrasenia"),
    path("historial/", views.historial, name="historial"),
    path("detalle/", views.detalle, name="detalle"),
    path("crud/", views.crud, name="crud"),
    path("v_add/", views.v_add, name="v_add"),
    path("v_find/<str:pk>", views.v_find, name="v_find"),
    path("v_upd/", views.v_upd, name="v_upd"),
    path("v_del/<str:pk>", views.v_del, name="v_del"),
]