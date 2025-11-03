from inventario.models import Producto

productos = [
    {"nombre": "Mouse", "descripcion": "Mouse óptico", "precio": 50.00 },
    {"nombre": "Teclado", "descripcion": "Teclado mecánico", "precio": 180.00 },
    {"nombre": "Monitor", "descripcion": "Monitor 24 pulgadas", "precio": 900.00 },
    {"nombre": "Audífonos", "descripcion": "Headset gamer", "precio": 120.00 },
    {"nombre": "Laptop", "descripcion": "Laptop Core i5", "precio": 2500.00 },
    {"nombre": "USB 32GB", "descripcion": "Memoria USB 32GB", "precio": 25.00 },
    {"nombre": "Webcam", "descripcion": "Webcam HD", "precio": 80.00 },
    {"nombre": "Silla Gamer", "descripcion": "Silla ergonómica", "precio": 600.00 },
    """ {"nombre": "Mouse", "descripcion": "Mouse óptico", "precio": 50.00, "stock": 20},
    {"nombre": "Teclado", "descripcion": "Teclado mecánico", "precio": 180.00, "stock": 10},
    {"nombre": "Monitor", "descripcion": "Monitor 24 pulgadas", "precio": 900.00, "stock": 5},
    {"nombre": "Audífonos", "descripcion": "Headset gamer", "precio": 120.00, "stock": 15},
    {"nombre": "Laptop", "descripcion": "Laptop Core i5", "precio": 2500.00, "stock": 8},
    {"nombre": "USB 32GB", "descripcion": "Memoria USB 32GB", "precio": 25.00, "stock": 50},
    {"nombre": "Webcam", "descripcion": "Webcam HD", "precio": 80.00, "stock": 12},
    {"nombre": "Silla Gamer", "descripcion": "Silla ergonómica", "precio": 600.00, "stock": 6}, """
]

for p in productos:
    Producto.objects.create(**p)

print("✅ Productos insertados correctamente")
