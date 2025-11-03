from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    # stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
