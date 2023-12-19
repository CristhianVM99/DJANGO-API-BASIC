from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from app_backend import views

router = routers.DefaultRouter()
router.register(r'cargos', views.CargoView, 'cargos')
router.register(r'genero', views.GeneroView, 'genero')
router.register(r'personalDeAtencion', views.PersonalDeAtencionView, 'personalDeAtencion')
router.register(r'marca', views.MarcaView, 'marca')
router.register(r'talla', views.TallaView, 'talla')
router.register(r'categoria', views.CategoriaView, 'categoria')
router.register(r'color', views.ColorView, 'color')
router.register(r'producto', views.ProductoView, 'producto')
router.register(r'cliente', views.ClienteView, 'cliente')
router.register(r'pago', views.PagoView, 'pago')
router.register(r'venta', views.VentaView, 'venta')

urlpatterns = [
    path('',include(router.urls)),
    path('docs/',include_docs_urls(title="Proyecto Documentacion"))
]