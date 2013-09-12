from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from datetime import datetime

from .models import Task

def home(request, name=None):
    if name:
        return HttpResponse("Django rocks! by %s" % name)
    else:
        return HttpResponse("I'm a rockstar")


def ticket_listing(request):
    objets = Task.objects.all().order_by('-due_date')
    return render_to_response('ticket/list.html', { 'objects': objets})


def ticket_detail(request, id):
    objet = Task.objects.get(pk=id)
    return render_to_response('ticket/detail.html', {'objet': objet})


def ticket_list(request):
    format = "%Y-%m-%d"
    objets = Task.objects.all()
    if request.method == 'GET':
        if 'closed' in request.GET:
            if request.GET['closed'] == 'true':
                objets = objets.filter(closed=True)
            else:
                objets = objets.filter(closed=False)
                if 'start' in request.GET and request.GET['start'] != '':
                    objets = objets.filter(
                        due_date__gte=datetime.strptime(
                            request.GET['start'], format)
                        )
                if 'end' in request.GET and request.GET['end'] != '':
                    objets = objets.filter(
                        due_date__lte=datetime.strptime(
                            request.GET['end'], format)
                        )
    return render(request, 'ticket/list.html',
                  { 'objets': objets },
                  )
                    


