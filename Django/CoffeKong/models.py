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

""" Destinatario """
class destinatario(models.Model):
    run_d = models.CharField(max_length=12, primary_key=True, db_column="run_d")
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)

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
    
""" Estado del pedido """
class estado(models.Model):
    id_estado = models.AutoField(primary_key=True, db_column="idEstado")
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return str(self.descripcion)

""" Pedido """
class pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True, db_column="idPedido")
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE, db_column="run")
    destinatario = models.ForeignKey("destinatario", on_delete=models.CASCADE, db_column="run_d")
    fecha = models.DateField()
    total_ped = models.IntegerField()
    estado = models.ForeignKey("estado", on_delete=models.CASCADE, db_column="idEstado")

    def __str__(self):
        return str(self.id_pedido)

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

""" Detalle pedido """
class detallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True, db_column="idDetalle")
    id_pedido = models.ForeignKey("pedido", on_delete=models.CASCADE, db_column="idPedido")
    id_producto = models.ForeignKey("producto", on_delete=models.CASCADE, db_column="idProducto")
    total = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.id_detalle)