from django.urls import path
from djmiddleware.views import index

urlpatterns = [
    path('', index), # type: ignore
]
