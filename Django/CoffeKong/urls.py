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
    path("contrasenia/", views.contrasenia, name="contrasenia"),
    path("historial/", views.historial, name="historial"),
    path("perfil/", views.perfil, name="perfil"),
    path("detalle/", views.detalle, name="detalle"),

    # Login
    path("login/", views.conectar, name="login"),
    path("logout/", views.desconectar, name="logout"),

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

    # Estados de pedido
    path("e_add/", views.e_add, name="e_add"),
    path("e_find/<str:pk>", views.e_find, name="e_find"),
    path("e_upd/", views.e_upd, name="e_upd"),
    path("e_del/<str:pk>", views.e_del, name="e_del"),

    # Pedidos
    path("p_add/", views.p_add, name="p_add"),
    path("p_find/<str:pk>", views.p_find, name="p_find"),
    path("p_upd/", views.p_upd, name="p_upd"),
    path("p_del/<str:pk>", views.p_del, name="p_del"),

    # Detalle de pedidos
    path("dt_add/", views.dt_add, name="dt_add"),
    path("dt_find/<str:pk>", views.dt_find, name="dt_find"),
    path("dt_upd/", views.dt_upd, name="dt_upd"),
    path("dt_del/<str:pk>", views.dt_del, name="dt_del"),

    # Productos
    path("pr_add/", views.pr_add, name="pr_add"),
    path("pr_find/<str:pk>", views.pr_find, name="pr_find"),
    path("pr_upd/", views.pr_upd, name="pr_upd"),
    path("pr_del/<str:pk>", views.pr_del, name="pr_del"),

    # Tipos de productos
    path("tp_add/", views.tp_add, name="tp_add"),
    path("tp_find/<str:pk>", views.tp_find, name="tp_find"),
    path("tp_upd/", views.tp_upd, name="tp_upd"),
    path("tp_del/<str:pk>", views.tp_del, name="tp_del"),

    # Proceso de compra
    path("load_carrito", views.load_carrito, name="load_carrito"),
    path("procesa_pedido", views.procesa_pedido, name="procesa_pedido"),
]