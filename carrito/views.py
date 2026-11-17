from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required
from catalogo.models import Libro
from django.contrib import messages

# Helpers
def _carrito_del_usuario(request) -> Carrito:
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user.perfil)
    return carrito

def _item_del_usuario(request, item_id):
    return get_object_or_404(
        ItemCarrito,
        id=item_id,
        carrito__usuario = request.user.perfil
    )
    
@login_required
def ver_carrito(request):
    carrito = _carrito_del_usuario(request)
    return render(request, 
                  "carrito/ver_carrito.html", 
                  {
                      'items':carrito.items.all(),
                      'total':carrito.total()
                   }
                  )
    
@login_required
def agregar_carrito(request, id):
    libro = get_object_or_404(Libro, pk=id)
    
    if libro.stock <= 0:
        messages.error(request, "No hay stock")
        return redirect('list-book')
    
    carrito = _carrito_del_usuario(request)
    
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, libro=libro)
    
    if not creado:
        # Item ya existe
        if item.cantidad < libro.stock:
            item.cantidad += 1
            item.save() # update
        else:
            messages.error(request, "No queda stock")
            
    return redirect('ver-carrito')

@login_required
def incrementar_item(request, id):
    item = _item_del_usuario(request, id)
    
    if item.cantidad < item.libro.stock:
        item.cantidad += 1
        item.save()
        
    return redirect('ver-carrito')

@login_required
def disminuir_item(request, id):
    item = _item_del_usuario(request, id)
    
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
        
    return redirect('ver-carrito')

@login_required
def eliminar_item(request, id):
    item = _item_del_usuario(request, id)
    
    item.delete()
        
    return redirect('ver-carrito')