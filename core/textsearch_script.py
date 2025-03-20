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
from textsearch.models import TextSearchProduct
import requests # type: ignore


url = "https://dummyjson.com/products?limit=5000"
response = requests.get(url)
data = response.json()


for product_data in data['products']:
    try:
        # print(product_data.get('brand'))
        product = TextSearchProduct(
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

# import random
# import uuid
# url = 'https://fakestoreapi.com/products'
# response = requests.get(url)
# products = response.json()

# for item in products:
#     product, created = TextSearchProduct.objects.get_or_create(
#         title=item['title'],
#         defaults={
#             'description': item['description'],
#             'category': item['category'],
#             'price': item['price'],
#             'thumbnail': item['image'],
#             'sku' : str(uuid.uuid4()).split('-')[0]
#         }
#     )