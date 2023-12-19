# cargo.py

from django.db import models

class Cargo(models.Model):
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return self.tipo

class Genero(models.Model):
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return self.tipo

class PersonalDeAtencion(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Talla(models.Model):
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Pago(models.Model):
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return self.tipo

class Venta(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    personal_de_atencion = models.ForeignKey(PersonalDeAtencion, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    def __str__(self):
        return self.cliente.nombre


