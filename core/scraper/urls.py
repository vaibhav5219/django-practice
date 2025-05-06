from django.urls import path
from .views import index, run_scraper

urlpatterns = [
    path('', index),
    path('run_scraper', run_scraper)
]