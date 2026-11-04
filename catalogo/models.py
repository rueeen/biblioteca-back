from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
            return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    publicacion = models.PositiveSmallIntegerField(verbose_name="Publicación")
    # Recomendados para auditoria
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    # nuevo atributo
    tapa_dura = models.BooleanField(default=False)
    # relaciones
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT, null=True)
    categoria = models.ManyToManyField(Categoria, null=True)
    # imagen libro
    portada = models.ImageField(upload_to="portadas", null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
