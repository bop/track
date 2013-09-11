from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Task

def home(request, name=None):
    if name:
        return HttpResponse("Django rocks! by %s" % name)
    else:
        return HttpResponse("I'm a rockstar")

def ticket_listing(request):
    objets = Task.objects.all().order_by('-due_date')
    return render_to_response('ticket/list.html', { 'objects': objets})
