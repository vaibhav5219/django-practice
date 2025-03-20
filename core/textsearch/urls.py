from django.urls import path
from textsearch.views import *


urlpatterns = [
    path("", index),
]
