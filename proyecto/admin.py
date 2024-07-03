from django.contrib import admin


from .models import Genero, Libro
# Register your models here.
admin.site.register(Genero)
admin.site.register(Libro)