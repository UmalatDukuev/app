from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello1")
    return render(request, 'autho/autho.html', {})
