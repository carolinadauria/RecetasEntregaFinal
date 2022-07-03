from datetime import datetime
from email.policy import default
from msilib.schema import ListView
from sqlite3 import Date
from django.db import models

from AppFinal.forms import recomendacionesFormulario, UserRegisterForm, UserCreationForm

# Create your models here.
class Recetas(models.Model):
    nombre = models.CharField(max_length=40)
    ingredientes = models.CharField(max_length=40)
    pasos = models.CharField(max_length=5000)
    
    def __str__(self) -> str:
        #return f"Receta: {self.nombre}\nIngredientes: {self.ingredientes}\nPasos: {self.pasos}"
        return self.nombre+"Ingredientes: "+str(self.ingredientes)+"Pasos: "+str(self.pasos)

class Recomendacion(models.Model):
    nombre = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=500)
    def __str__(self) -> str:
        return "Producto: "+str(self.nombre)+"Comentarios: "+str(self.comentarios)





