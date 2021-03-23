from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
   path('',Home.as_view(), name='Index'),  
   path('contacto/', Contacto.as_view(), name='contactos')
    
     
   ]