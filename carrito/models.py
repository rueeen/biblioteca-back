from django.db import models
from registro.models import Perfil
from catalogo.models import Libro

# Create your models here.
class Carrito(models.Model):
    usuario = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    # relacion foreignkey
    # items = []

    def total(self):
        total = 0
        for i in self.items.all():
            total += i.sub_total()
        return total

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def sub_total(self):
        return self.cantidad * self.libro.precio

class Pedido(models.Model):
    pass