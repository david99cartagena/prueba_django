from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from getpass import getpass


class Command(BaseCommand):
    help = "Crear usuario desde consola"

    def handle(self, *args, **kwargs):
        self.stdout.write("=== CREAR USUARIO ===")

        username = input("Usuario: ")
        email = input("Email: ")
        password = getpass("Contraseña: ")
        is_admin = input("¿Es admin? (s/n): ").lower() == "s"

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR("El usuario ya existe ⚠️"))
            return

        if is_admin:
            User.objects.create_superuser(
                username=username, email=email, password=password
            )
            self.stdout.write(self.style.SUCCESS("Superusuario creado ✅"))
        else:
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Usuario creado ✅"))
