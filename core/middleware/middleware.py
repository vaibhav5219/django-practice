# IP wBlocking

'''
    def __init__(self, get_response) => One time initialization of custom middleware
    def __call__(self, request)      => Code that is executed in each request before and after the view is called
    process_request         =>     Url pe jane ke pahle eska code chalega
    process_view            =>     Url pe jane ke baad aur view pe jane ke phale eska code execute hoga
    process_response        =>   After the view is called; this can modify or even return a new response.
    process_exception       =>      Koi bhi exception pe ye code run hoga
'''


from typing import Any
from django.http import HttpResponseForbidden
from djmiddleware.models import Store

ALLOWED_IP = ["123.45.67.89", "987.56.65.21"]  # , "127.0.0.1"
class IPBlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def __call__(self, request):
        ip = self.get_client_ip(request)
        print("Ip =>>>>>", ip)
        if ip in ALLOWED_IP:
            return HttpResponseForbidden("Ip Not Allowed")
        response = self.get_response(request)

        return response
    

class CheckBmpHeader:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        headers = request.headers

        if "bmp" not in headers:
            return HttpResponseForbidden("Bmp Id not found")
        else:
            if not Store.objects.filter(bmp_id = request.header.get('bmp') ):
                return HttpResponseForbidden("Wrong bmp Id")
        return self.get_response(request)
    


'''
#############################  CLASS BASED MIDDLEWARE #######################################
class ExampleMiddleware:

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):

        # Code that is executed in each request before the view is called

        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response

    def process_view(request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
    
    def process_request(self, request):
        pass

    def process_response(self, request):
        pass

    def process_exception(request, exception):
        # This code is executed if an exception is raised

    def process_template_response(request, response):
        # This code is executed if the response contains a render() method
        return response'
'''


'''
###################################### FUNCTION BASED MIDEELEWARE #################################
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
'''