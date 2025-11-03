from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nuevo/", views.crear_producto, name="crear_producto"),
    path("api/productos/", views.api_productos, name="api_productos"),
    path("editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
]