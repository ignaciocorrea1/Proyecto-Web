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
    # Crud
    path("crud/", views.crud, name="crud"),
    # Vendedores
    path("v_add/", views.v_add, name="v_add"),
    path("v_find/<str:pk>", views.v_find, name="v_find"),
    path("v_upd/", views.v_upd, name="v_upd"),
    path("v_del/<str:pk>", views.v_del, name="v_del"),
    # Clientes
    path("c_add/", views.c_add, name="c_add"),
    path("c_find/<str:pk>", views.c_find, name="c_find"),
    path("c_upd/", views.c_upd, name="c_upd"),
    path("c_del/<str:pk>", views.c_del, name="c_del"),
    # Tarjetas de clientes
    path("tc_add/", views.tc_add, name="tc_add"),
    path("tc_find/<str:pk>", views.tc_find, name="tc_find"),
    path("tc_upd/", views.tc_upd, name="tc_upd"),
    path("tc_del/<str:pk>", views.tc_del, name="tc_del"),
    # Pedidos
    path("p_add/", views.p_add, name="p_add"),

]