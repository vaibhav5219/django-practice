import os

import django
import itertools
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()
import django
import random
from faker import Faker

from datetime import datetime, timedelta
from django.db.models import Avg, Sum, Min, Max, Count, Q
from django.db.models import Subquery, OuterRef
from elasticsearch_app.models import Product, Brand
import requests

'''
DELETE Product manualy/using script

'''
# from elasticsearch_app.documents import ProductDocument
# from elasticsearch_app.models import Product

# product = Product.objects.get(id=170)
# product.title = "No Title"
# product.save()

# ProductDocument().delete(id=170)



''' Add Data into Product Table  '''


url = "https://dummyjson.com/products?limit=5000"
response = requests.get(url)
data = response.json()


for product_data in data['products']:
    try:
        # print(product_data.get('brand'))
        product = Product(
            title=product_data['title'],
            description=product_data['description'],
            category=product_data['category'],
            price=product_data['price'],
            brand=product_data.get('brand'),
            sku=product_data['sku'],
            thumbnail=product_data['thumbnail']
        )
        product.save()

    except Exception as e:
        print(e)


products = Product.objects.all()

for product in products:
    try:
        brand , _ = Brand.objects.get_or_create(brand_name = product.brand)
        product.brand_name = brand
        product.save()
    except Exception as e:
        print(e)