
from .models import Libro, Genero
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm  # Importa el formulario
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.



def index(request):
    libros= Libro.objects.all()
    context={"libros":libros}
    return render(request, 'proyecto/inicio.html', context)


@login_required
def libro1(request):

    context={}

    return render(request, 'proyecto/libro1.html', context)

@login_required
def libro2(request):

    context={}

    return render(request, 'proyecto/libro2.html', context)

@login_required
def libro3(request):

    context={}

    return render(request, 'proyecto/libro3.html', context)

@login_required
def portadas(request):
    context={}

    return render(request, 'proyecto/portadas.html', context)

@login_required
def crud(request):
    libros = Libro.objects.all()
    context = {'libros': libros}
    return render(request, 'proyecto/libro_list.html', context)

@login_required
def librosAdd(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'proyecto/libro_add.html', context)
    
    else:

        nombre=request.POST["nombre"]
        fecha=request.POST["fecha"]
        genero=request.POST["genero"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Libro.objects.create(nombre=nombre,
                                 fecha=fecha,
                                 id_genero=objGenero,
                                 activo=1 )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'proyecto/libro_add.html', context)


@login_required
def libros_del(request,pk):
    context={}
    try:
        libro=Libro.objects.get(nombre=pk)
        libro.delete()
        mensaje="Bien, datos eliminados..."
        libros = Libro.objects.all()
        context = {'libros': libros, 'mensaje': mensaje}
        return render (request, 'proyecto/libro_list.html', context) 
    except:
        mensaje = "No hay libros disponibles..."
        libros = Libro.objects.all()
        context = {'libros': libros, 'mensaje': mensaje}
        return render (request, 'proyecto/libro_list.html', context)
    
@login_required
def libros_findEdit(request,pk):
    if pk != "":
        libro=Libro.objects.get(nombre=pk) 
        generos= Genero.objects.all()
        print(type (libro.id_genero.genero))
        context={'libro':libro, 'generos': generos}
        if libro:      
            return render(request, 'proyecto/libro_edit.html', context)
        else:
            context={ 'mensaje': "Error, id no existe..."}
            return render (request, 'proyecto/libro_list.html', context)


@login_required      
def librosUpdate(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        fecha=request.POST["fecha"]
        genero=request.POST["genero"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        libro = Libro()
        libro.nombre = nombre
        libro.fecha = fecha
        libro.id_genero =objGenero
        libro.activo=1
        libro.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok , datos actualizados...",'generos':generos,'libro':libro }
        return render(request, 'proyecto/libro_edit.html',context)
    else:
        libros = Libro.objects.all()
        context={'libros': libros}
        return render(request, 'proyecto/libro_list.html', context)



def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}!")
            return redirect("inicio")  # redireccion a la pagina de inicio :)
    else:
        form = RegistroForm()
    return render(request, "registration/register.html", {"form": form})