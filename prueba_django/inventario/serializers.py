from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ["id", "nombre", "descripcion", "precio", "fecha_creacion"]
        fields = "__all__"  # No cambia si ya usas __all__
