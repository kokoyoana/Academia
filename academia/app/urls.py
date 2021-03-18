from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('index', Index.as_view(), name='inicio'),

     
     
    ]