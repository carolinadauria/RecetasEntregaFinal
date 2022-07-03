from django.urls import path
from AppFinal.views import inicio, login_request, recetas, contacto, conocenos, recomendacionFormulario, login_request, register, editarPerfil, leerRecomendaciones, eliminarRecomendacion, eliminarPerfil, editarRecomendacion, detalleReceta1, detalleReceta2, detalleReceta3, RecomendacionDetalle

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name='Inicio'),
    path('recetas/', recetas, name='Recetas'),
    path('contacto/', contacto, name='Contacto'),
    path('conoceme/', conocenos, name='Conoceme'),
    path('recomendacion/nuevarecomendacion', recomendacionFormulario, name='RecomendacionFormulario'),
    path('recomendaciones', leerRecomendaciones, name='Recomendaciones'),
    path('eliminarrecomendacion/<nombre>', eliminarRecomendacion, name='EliminarRecomendacion'),
    path('editarrecomendacion/<nombre>', editarRecomendacion, name='EditarRecomendacion'),
    path('login', login_request, name='Login'),
    path('register', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html')),
    path('login?next=/editarperfil', editarPerfil, name='EditarPerfil'),
    path('editarperfil', editarPerfil, name='EditarPerfil'),
    path('editarperfil/<username>', eliminarPerfil, name='EliminarPerfil'),
    path('recomendaciones/<nombre>', RecomendacionDetalle.as_view(), name='DetalleRecomendacion'),
    path('recetas/budindelimon', detalleReceta1,name='Receta1'),
    path('recetas/muffinarandanos', detalleReceta2,name='Receta2'),
    path('recetas/alitascoliflor', detalleReceta3,name='Receta3'),
    ]