import json
import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from GeekShop.settings import BASE_DIR
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

FILE_PATH = BASE_DIR / 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + ".json")) as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete()
        for cat in categories:
            # ProductCategory.objects.create(**cat)
            new_cat = ProductCategory(**cat)
            new_cat.save()

        products = load_from_json("products")
        Product.objects.all().delete()
        for prod in products:
            cat_name = prod['category']
            _cat = ProductCategory.objects.get(name=cat_name)
            prod['category'] = _cat
            Product.objects.create(**prod)

        ShopUser.objects.create_superuser(username='django', password='geekbrains', age=30)