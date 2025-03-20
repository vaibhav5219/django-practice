from django.http import HttpResponseForbidden

ALLOWED_IP = ["123.45.55", '3344.456.55']

class IPBlockingMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __call__(self, request):
        ip = self.get_client_ip(request) # request.META.get('REMOTE_ADDR')
        print('ip =>> ',ip)
        if ip in ALLOWED_IP:
            return HttpResponseForbidden("Forbidden: IP not allowed")
        
        return self.get_response