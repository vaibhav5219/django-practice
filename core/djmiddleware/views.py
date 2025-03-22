from django.shortcuts import render
from django.http import JsonResponse
from djmiddleware.models import Store

def index(request):
    print (request.headers.get('bmp'))
    store = Store.objects.filter(bmp_id = request.heeaders.get('bmp'))
    data = {
        'status': True,
        'data': {
            'bmp_id' : store.bmp_id, # type: ignore
            'store_name': store.store_name,  # type: ignore
        }
    }
    return JsonResponse(data)