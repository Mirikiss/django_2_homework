from django.core.management.base import BaseCommand
from shop.shopmen.models import Client

class Command(BaseCommand):
    help = 'Create base'

    def handle(self, *args, **options):
        client = Client(name='Pavel', email='123@mail.ru', phone='123123123', address='mozir', )
        client.save()
        self.stdout.write(f'{client}')