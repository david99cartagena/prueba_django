# prueba_django

1. Instalar virtualenv (opcional)

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

5. Crear migraciones (a partir de tus modelos)

```cmd
python manage.py makemigrations
```

6. Aplicar las migraciones a la base de datos

```cmd
python manage.py migrate
```

7. Creacion de usuario de Pruebas

```cmd
python manage.py seedadmin
```

8. Creacion de Productos de Inventario

```cmd
python manage.py shell < inventario/seedproducto.py
```

9. Iniciar proyecto creado

```cmd
python manage.py runserver
```
