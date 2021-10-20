from django.db import models
from datetime import timedelta

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=40)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='media/productos', null=True)
    publicado = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)

class Arriendo(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    telefono = models.IntegerField()
    precio = models.IntegerField(null = True)
    tipobici = models.CharField(max_length=50, null= True)
    fecha_arriendo = models.DateField(null=True)
    fecharetiro = models.DateTimeField(null=True)
    fechaentrega = models.DateTimeField(null=True)
    comentarios = models.TextField(null = True)
    Cancelado = models.BooleanField(default=False)
    Entregado = models.BooleanField(default=False)
    Finalizado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)

class Reparacion(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(null = True)
    foto = models.ImageField(upload_to='media/reparacion', null=True)
    fecha_salida = models.DateField(null = True)
    detalle_cliente = models.TextField(null = True)
    Detalle_tecnico = models.TextField(null = True)
    precio = models.IntegerField(null = True)
    ingreso = models.BooleanField(default=False)
    en_reparacion = models.BooleanField(default=False)
    entregada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)
