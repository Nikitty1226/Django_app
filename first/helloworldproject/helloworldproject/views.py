from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnobject = HttpResponse('hello world')
    return returnobject

class helloworldclass(TemplateView):
    template_name = "hello.html"