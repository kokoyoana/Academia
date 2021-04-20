from django.urls import path, include
from .views import *
from . import views

#EN CONSTRUCCION POR RA
from django.contrib.auth.views import LogoutView,LoginView



urlpatterns = [
   path('', Home.as_view(), name='Index'),  
   path('inicio/', Home.as_view(), name='inicio'),  
   path('contacto/',Contacto.as_view(), name='contactos'),
   path('quienes/',Quien.as_view(), name='quien'),
   path('cursos/',Cursos.as_view(), name='curso'),
   path('curso/<int:pk>/',InfoCurso.as_view(), name='infocurso'),
   

   ]




   