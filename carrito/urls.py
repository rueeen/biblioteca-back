from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver-carrito'),
    path('carrito/agregar/<int:id>/', views.agregar_carrito, name='agregar-carrito'),
    path('carrito/incrementar/<int:id>/', views.incrementar_item, name='incrementar-carrito'),
    path('carrito/disminuir/<int:id>/', views.disminuir_item, name='disminuir-carrito'),
    path('carrito/eliminar/<int:id>/', views.eliminar_item, name='eliminar-carrito'),
]
