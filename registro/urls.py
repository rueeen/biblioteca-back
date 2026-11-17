from django.urls import path
from . import views

urlpatterns = [
    path("cuentas/login/", views.login_view, name='login'),
    path("cuentas/logout/", views.logoutView, name='logout'),
    path("cuentas/registrar/", views.registrar_view, name='registrar'),
    path("cuentas/error/403", views.error403View, name='403'),
]
