# 📝 Inventario Producto Django

Inventario Producto Django es una **Mini-Aplicación Web** que permite gestionar productos de un inventario.

- Los usuarios pueden registrarse, iniciar sesión y realizar operaciones de **CRUD (crear, leer, actualizar y eliminar productos).**
- La aplicación incluye autenticación de usuarios, paginación en el listado de productos y una **API REST** protegida que devuelve los productos en formato **JSON.**
- Además, se utilizan alertas interactivas con **SweetAlert2** para mejorar la experiencia del usuario y **Bootstrap** para un diseño responsive.

## 🖼️ Imagenes de la Aplicacion

- **Login**

  - **Usuario:** admintest
  - **Password:** admin123
    ![Login](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_6.png)

- **Modulo Inventario**
  ![Modulo Inventario](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_7.png)
  - **Crear Producto**
    ![Crear Producto](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_8.png)
    ![Crear Producto](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_9.png)
  - **Editar Producto**
    ![Editar Producto](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_10.png)
  - **Eliminar Producto**
    ![Eliminar Producto](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_11.png)

## ⚙️ Tecnologías Utilizadas

- **Python 3.12**
- **Django 5.2.7**
- **Javascript**
- **SweetAlert2**
- **HTML5 / CSS3**
- _asgiref 3.10.0_
- _djangorestframework 3.16.1_
- _sqlparse 0.5.3_
- _tzdata 2025.2_

## 📁 Estructura del Proyecto

```
/prueba_django
├── .gitignore
├── README.md
├── venv/                     # Entorno virtual (no se sube a Git)
├── media/                    # Archivos (imágenes de construccion y visualizacion del proyecto, etc.)
│
├── prueba_django/            # Carpeta raíz del proyecto
│   ├── manage.py             # Script principal para ejecutar comandos Django
│   ├── db.sqlite3            # Base de datos SQLite
│   ├── requirements.txt      # Dependencias del proyecto
│   │
│   ├── templates/            # Plantillas HTML (Frontend)
│   │   ├── base.html         # Template base con Bootstrap y navbar
│   │   ├── inventario/       # Templates del módulo Inventario
│   │   │   ├── index.html        # Página principal del inventario
│   │   │   └── product_form.html # Formulario para productos
│   │   └── registration/
│   │       └── login.html    # Template de login (Django auth)
│   │
│   ├── inventario/           # App principal
│   │   ├── admin.py          # Registro de modelos para Django admin
│   │   ├── apps.py           # Configuración de la app
│   │   ├── models.py         # Modelos de base de datos
│   │   ├── views.py          # Controladores / lógica de vistas
│   │   ├── urls.py           # Rutas de la app
│   │   ├── forms.py          # Formularios Django
│   │   ├── serializers.py    # Serializadores para API / DRF
│   │   ├── tests.py          # Tests unitarios
│   │   │
│   │   ├── migrations/       # Migraciones de BD generadas por Django
│   │   │
│   │   ├── management/       # Scripts personalizados Django
│   │   │   └── commands/     # Comandos tipo "seeders"
│   │   │       ├── seedadmin.py     # Crea un usuario administrador
│   │   │       ├── seeduser.py      # Crea un usuario normal (cliente/empleado)
│   │   ├── seedproducto.py   # Carga productos iniciales
│   │
│   └── prueba_django/        # Configuración principal del proyecto
│       ├── settings.py       # Configuración general de Django
│       ├── urls.py           # Rutas globales del proyecto
│       ├── wsgi.py           # Configuración para despliegue WSGI
│       └── asgi.py           # Configuración para despliegue ASGI
```

## ✅ Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu entorno:

- Python version 3.12

## 📦 Instalación Local Windows

1. Instalar virtualenv ( Opcional )

```cmd
pip install virtualenv
```

2. Crear el entorno virtual

```cmd
python -m venv venv
```

3. Activar el entorno virtual

```cmd
venv\Scripts\activate
```

4. leer e instalar las dependencias

```cmd
cd prueba_django
```

```cmd
pip install -r requirements.txt
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_1.png)

5. Crear migraciones (a partir de tus modelos)

```cmd
python manage.py makemigrations
```

6. Aplicar las migraciones a la base de datos

```cmd
python manage.py migrate
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_2.png)

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_3.png)

7. Creacion de usuario de Pruebas

```cmd
python manage.py seedadmin
```

8. Creacion de Productos de Inventario

```cmd
python manage.py shell < inventario/seedproducto.py
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_4.png)

9. Creacion de usuario de Pruebas ( Opcional )

```cmd
python manage.py seeduser
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_12.png)

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_13.png)

10. Validar las dependecias ( Opcional )

```cmd
pip freeze
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_14.png)

11. Iniciar proyecto creado

```cmd
python manage.py runserver
```

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_5.png)

![](https://raw.githubusercontent.com/david99cartagena/prueba_django/refs/heads/main/media/Screenshot_6.png)
