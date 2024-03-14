from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Inicio")

def pagina1(request):
    return HttpResponse("Jepe")

def pagina2(request):
    return HttpResponse("Manu")