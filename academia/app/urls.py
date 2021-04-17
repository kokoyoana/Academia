from django.urls import path, include
from .views import *
from . import views

#EN CONSTRUCCION POR RA
from django.contrib.auth.views import LogoutView



urlpatterns = [
   path('', Home.as_view(), name='Index'),  
   path('inicio/', Home.as_view(), name='inicio'),  
   path('contacto/',Contacto.as_view(), name='contactos'),
   path('cursos/',Cursos.as_view(), name='curso'),
   path('quienes/',Quien.as_view(), name='quien'),
   path('curso/<int:pk>/',InfoCurso.as_view(), name='infocurso'),

   #EN CONTRUCCION POR RA  
   path('login/', Login_View.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout') #listo

   


    
     
   ]




   