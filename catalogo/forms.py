from .models import Libro, Autor, Categoria
from django import forms

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        #fields = ['id', 'titulo', 'descripcion', '']
        fields = '__all__'
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"