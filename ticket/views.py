from django.http import HttpResponse

def home(request, name=None):
    if name:
        return HttpResponse("Django rocks! by %s" % name)
    else:
        return HttpResponse("I'm a rockstar")
