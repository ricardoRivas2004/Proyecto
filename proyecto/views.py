from django.shortcuts import render
from .models import Genero, Libro
# Create your views here.


def index(request):
    libros= Libro.objects.all()
    context={"libros":libros}
    return render(request, 'proyecto/inicio.html', context)


def login(request):

    context={}

    return render(request, 'proyecto/login.html', context)


def register(request):

    context={}

    return render(request, 'proyecto/register.html', context)


def libro1(request):

    context={}

    return render(request, 'proyecto/libro1.html', context)

def libro2(request):

    context={}

    return render(request, 'proyecto/libro2.html', context)

def libro3(request):

    context={}

    return render(request, 'proyecto/libro3.html', context)

def portadas(request):
    context={}

    return render(request, 'proyecto/portadas.html', context)

