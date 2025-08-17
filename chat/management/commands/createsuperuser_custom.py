from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with a default password'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            # Create the user first
            user = User.objects.create_superuser(
                username='admin',
                password='admin123'
            )
            # Set additional fields after creation
            user.tokens = 10000
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists!'))
