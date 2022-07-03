from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from AppFinal.models import Recetas, Recomendacion
from django.template import loader
from AppFinal.forms import recomendacionesFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

# Create your views here.
def inicio(self):
    plantilla = loader.get_template('AppFinal/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def recetas(request):
    return render(request, 'AppFinal/recetas.html')

def detalleReceta1(request):
    return render(request, 'AppFinal/receta1.html')

def detalleReceta2(request):
    return render(request, 'AppFinal/receta2.html')

def detalleReceta3(request):
    return render(request, 'AppFinal/receta3.html')


def contacto(request):
    return render(request, 'AppFinal/contacto.html')

def conocenos(request):
    return render(request, 'AppFinal/conocenos.html')

def recomendacionFormulario(request):
    if request.method == 'POST':
        miFormulario = recomendacionesFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = request.POST['nombre']
            comentarios = request.POST['comentarios']
            recomendacion = Recomendacion(nombre=nombre, comentarios=comentarios)
            recomendacion.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = recomendacionesFormulario()
    return render(request, "AppFinal/recomendacionFormulario.html", {"miFormulario":miFormulario})


class RecomendacionesList(ListView):
    model = Recomendacion
    template_name = "AppFinal/recomendaciones_list.html"



def leerRecomendaciones(request):
    recomendaciones = Recomendacion.objects.all()
    nombre = Recomendacion.nombre
    comentarios = Recomendacion.comentarios
    contexto = {'nombre':nombre, 'comentarios':comentarios, 'recomendaciones':recomendaciones}
    return render(request, "AppFinal/leerRecomendaciones.html", contexto)

class RecomendacionDetalle(DetailView):
    model = Recomendacion
    template_name = "AppFinal/detallerecomendacion.html"
    def get_object(self):
        return Recomendacion.objects.get(nombre=self.kwargs.get("nombre"))

class RecomendacionesList(DeleteView, LoginRequiredMixin):
    model = Recomendacion
    success_url = "AppFinal/recomendaciones/list"
    def get_object(self):
        return Recomendacion.objects.get(nombre=self.kwargs.get("nombre"))



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=pwd)

            if user is not None:
                login(request, user)

                return render(request, "AppFinal/inicio.html", {"mensaje":f"Bienvenidx {usuario}"})
            else:
                return render(request, "AppFinal/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
                return render(request, "AppFinal/inicio.html", {"mensaje":"Error, datos incorrectos"})
    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {'form':form})



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppFinal/inicio.html", {"mensaje":"Usuario Creado"})
    else:
        form = UserRegisterForm()
    return render(request, "AppFinal/registro.html", {"form":form})



@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def eliminarPerfil(request, username):
    username = User.objects.get(username=username)
    username.delete()
    usuarios = User.objects.all()
    contexto = {'usuarios':usuarios}
    return render(request, "AppFinal/inicio.html", contexto)


@login_required
def eliminarRecomendacion(request, nombre):
    recomendacion = Recomendacion.objects.get(nombre=nombre)
    recomendacion.delete()
    recomendaciones = Recomendacion.objects.all()
    contexto = {'recomendaciones':recomendaciones}
    return render(request, "AppFinal/leerRecomendaciones.html", contexto)

@login_required
def editarRecomendacion(request, nombre):
    recomendacion = Recomendacion.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = recomendacionesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            recomendacion.nombre = informacion['nombre']
            recomendacion.comentarios = informacion['comentarios']
            recomendacion.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = recomendacionesFormulario(initial={'nombre':recomendacion.nombre, 'comentarios':recomendacion.comentarios})

    return render(request, "AppFinal/editarRecomendacion.html", {"miFormulario":miFormulario, "nombre":nombre})
