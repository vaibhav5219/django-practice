import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"
django.setup()
from datetime import datetime, timedelta
from django.db.models import Avg, Count, Min, Max, Count, Sum, Q, Subquery, OuterRef
import random
from home.models import Product, Brand



Product.objects.create(brand = Brand.objects.first(), product_name = "timer men with extra blade")

