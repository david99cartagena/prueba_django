from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Crea un superusuario de prueba"

    def handle(self, *args, **options):
        username = "admintest"
        email = "admin@test.com"
        password = "admin123"

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("⚠️ El usuario admin de prueba ya existe.")
            )
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS("✅ Usuario admin creado correctamente"))
