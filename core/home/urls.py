from django.urls import path, include
from home.views import *


urlpatterns = [
    path('',search_page),
]