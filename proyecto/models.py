from django.db import models

# Create your models here.

class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)  
    nombre          = models.CharField(max_length=30)
    fecha_publicado = models.DateField(blank=False, null=False)
    id_genero       = models.ForeignKey('genero',on_delete=models.CASCADE, db_column='idGenero')
    activo          = models.IntegerField() 

def __str__(self):
    return str(self.nombre)

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

def __str__(self):
    return str(self.genero)