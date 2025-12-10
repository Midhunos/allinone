from django.conf import settings
from django.http import HttpResponseForbidden

class BlockIPMiddleware:
    """
    Middleware to block requests from specific IP addresses.
    The blocked IPs are defined in the Django settings as BLOCKED_IPS.
    """

    def __init__(self, get_response):
        self.get_response=get_response
        self.blocked_ips = getattr(settings, 'BLOCKED_IPS_LIST', [])


    def __call__(self, request):
        ip=self.get_client_ip(request)
        print("CLIENT IP:", ip)  # DEBUG LINE
        if ip in self.blocked_ips:
           return HttpResponseForbidden("Access denied this ip.")
        return self.get_response(request)
    
    def get_client_ip(self,request):
        x_forwarded_for=request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")
    
