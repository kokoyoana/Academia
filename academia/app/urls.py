from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
   path('',Home.as_view(), name='Index'),  
   path('inicio/',Home.as_view(), name='inicio'),  
   path('contacto/',Contacto.as_view(), name='contactos'),
   path('cursos/',Cursos.as_view(), name='curso'),
   path('quienes/',Quien.as_view(), name='quien'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout')

   


    
     
   ]




   