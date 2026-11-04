from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    # Libro urls
    path("libros/", views.bookListView, name="list-book"),
    path("libros/crear/", views.bookCreateView, name="create-book"),
    path("libros/eliminar/<int:id>/", views.bookDeleteView, name="delete-book"),
    path("libros/actualizar/<int:id>/", views.bookUpdateView, name="update-book"),
    path("libros/detalle/<int:id>/", views.bookDetailView, name="detail-book"),
    # Author urls
    path("autores/", views.authorListView, name="list-author"),
    path("autores/crear", views.authorCreateView, name="create-author"),
    # Category urls
    path("categorias/", views.categoryListView, name="list-category"),
    path("categorias/crear", views.categoryCreateView, name="create-category"),
]
