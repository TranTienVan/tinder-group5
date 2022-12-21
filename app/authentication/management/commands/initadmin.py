from django.core.management.base import BaseCommand
from ...models import CustomUser
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            email = os.environ.get("SUPER_USER_EMAIL")
            password = os.environ.get("SUPER_USER_PASSWORD")
            print('Creating account for %s (%s)' % (email, password))
            admin = CustomUser.objects.create_superuser(email = email,password = password)
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')