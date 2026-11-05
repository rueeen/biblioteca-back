from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Categoria
from .forms import LibroForm, AutorForm, CategoriaForm
from django.contrib import messages

# Create your views here.
def homeView(request):
    return render(request, "catalogo/base.html")

################## VISTAS LIBRO ##################

def bookListView(request):
    if not request.user.is_authenticated:
        return redirect('403')
    
    listado = Libro.objects.all() # -> SELECT * FROM Libro
    return render(request, "catalogo/books/book_list.html", {"listado": listado})

def bookCreateView(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            # guardar libro en base de datos
            # INSERT INTO Libro(titulo, descrip...)
            form.save()
            messages.success(request, "Libro creado")
            return redirect('list-book')
        messages.error(request, "Libro no se pudo crear")
    return render(request, "catalogo/books/book_form.html", {'form':form, 'accion':'Crear'})

def bookDeleteView(request, id):
    # SELECT * FROM Libro WHERE id = id
    libro = get_object_or_404(Libro, pk=id)
    if request.method == "POST":
        # DELETE FROM Libro WHERE id = id
        libro.delete()
        messages.success(request, "Libro eliminado")
        return redirect('list-book')
    return render(request, "catalogo/books/book_delete.html")

def bookUpdateView(request, id):
    libro = get_object_or_404(Libro, pk=id)
    form = LibroForm(request.POST or None, request.FILES or None,instance=libro)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado")
            return redirect('list-book')
    return render(request, "catalogo/books/book_form.html", {"form":form, "accion":"Actualizar"})

def bookDetailView(request, id):
    book = get_object_or_404(Libro, pk=id)
    return render(request, "catalogo/books/book_detail.html", {"book":book})

################## VISTAS AUTOR ##################

def authorListView(request):
    return render(request, "catalogo/authors/author_list.html", {"listado":Autor.objects.all()})

def authorCreateView(request):
    form = AutorForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado")
            return redirect("list-author")
        
        messages.error(request, "Autor no se pudo crear")
    return render(request, "catalogo/authors/author_form.html", {"form":form, "accion":"Crear"})


################## VISTAS CATEGORIA ##################

def categoryListView(request):
    return render(request, "catalogo/category/category_list.html", {"listado":Categoria.objects.all()})

def categoryCreateView(request):
    form = CategoriaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria creada")
            return redirect("list-category")
        
        messages.error(request, "Categoria no se pudo crear")
    return render(request, "catalogo/category/category_form.html", {"form":form, "accion":"Crear"})

