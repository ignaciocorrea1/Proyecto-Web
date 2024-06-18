from django.db import models

# Create your models here.
    
""" Cliente """
class cliente(models.Model):
    run = models.CharField(max_length=12, primary_key=True, db_column="run")
    nombres = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombres+" "+self.apaterno+" "+self.amaterno)

""" Vendedor """
class vendedor(models.Model):
    run = models.CharField(max_length=12, primary_key=True, db_column="run")
    nombres = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombres+" "+self.apaterno+" "+self.amaterno)

""" Tarjeta """
class tarjeta(models.Model):
    nro_tarjeta = models.CharField(primary_key=True, db_column="nroTarjeta", max_length=30)
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE, db_column="run")

    def __str__(self):
        return str(self.nro_tarjeta)

""" Tipo de producto """
class tipoProducto(models.Model):
    id_tipoproducto = models.CharField(max_length=2, primary_key=True, db_column="idTipoProducto")
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return str(self.descripcion)

""" Producto """
class producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, db_column="idProducto")
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=100)
    tipo = models.ForeignKey("tipoProducto", on_delete=models.CASCADE, db_column="idTipoProducto")

    def __str__(self):
        return str(self.id_producto)

""" Pedido """
class pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True, db_column="idPedido")
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE, db_column="run")
    fecha = models.DateField()

    def __str__(self):
        return str(self.id_pedido)

""" Detalle pedido """
class detallePedido(models.Model):
    id_pedido = models.ForeignKey("pedido", on_delete=models.CASCADE, db_column="idPedido")
    id_producto = models.ForeignKey("producto", on_delete=models.CASCADE, db_column="idProducto")
    total = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.id_pedido)