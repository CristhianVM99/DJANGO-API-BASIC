from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CargoSerializer,GeneroSerializer,PersonalDeAtencionSerializer,MarcaSerializer,TallaSerializer,CategoriaSerializer,ColorSerializer,ProductoSerializer,ClienteSerializer,PagoSerializer,VentaSerializer
from .models import Cargo,Genero,PersonalDeAtencion,Marca,Talla,Categoria,Color,Producto,Cliente,Pago,Venta

class CargoView(viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()

class GeneroView(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()

class PersonalDeAtencionView(viewsets.ModelViewSet):
    serializer_class = PersonalDeAtencionSerializer
    queryset = PersonalDeAtencion.objects.all()

class MarcaView(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()

class TallaView(viewsets.ModelViewSet):
    serializer_class = TallaSerializer
    queryset = Talla.objects.all()

class CategoriaView(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class ColorView(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class PagoView(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()

class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
