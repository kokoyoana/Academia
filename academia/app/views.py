from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType
from django.views.generic import *
from .models import *
from django.http import HttpResponseRedirect
from .forms import Formulario
from django.forms import MultipleChoiceField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from random import choices
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
#EN COSTRUCCION POR RA
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.
class Home(TemplateView):
    template_name='app/index.html'

    def get_context_data(self,**kwargs):
        context=super(Home, self).get_context_data(**kwargs)
        context['contact_form'] = Formulario()
        context['cursos'] = Curso.objects.all()
 
        return context

    def post(self, request,*args,**kwargs):
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
      

        body= render_to_string(
            'app/email_content.html', {
                'nombre':nombre,
                'mensaje':mensaje,
                'email':email,
                'telefono':telefono,
                
            },
        )

        print(nombre)

        email_message = EmailMessage(
            subject='mensaje de usuario',
            body=body,
            from_email=email,
            to=['kokoyoana8@gmail.com'],
        )
        email_message.content_subtype='html'
        email_message.send()
        return redirect('app:inicio')


  


    
class Cursos(TemplateView):
    template_name='app/cursos.html'
    model = Curso

    def get_context_data(self,**kwargs):
        context=super(Cursos, self).get_context_data(**kwargs) 
        context['cursos']= Curso.objects.all()

        return context


class Contacto(TemplateView):
    template_name = 'app/contacto.html'
    
  

    def get_context_data(self,**kwargs):
        context=super(Contacto, self).get_context_data(**kwargs)
        context['contact_form'] =Formulario()
 
        return context

    def post(self, request,*args,**kwargs):
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
      

        body= render_to_string(
            'app/email_content.html', {
                'nombre':nombre,
                'mensaje':mensaje,
                'email':email,
                'telefono':telefono,
                
            },
        )

        print(nombre)

        email_message = EmailMessage(
            subject='mensaje de usuario',
            body=body,
            from_email=email,
            to=['kokoyoana8@gmail.com'],
        )
        email_message.content_subtype='html'
        email_message.send()
        return redirect('app:inicio')

class Quien(TemplateView):
    template_name='app/quienes.html'


    def get_context_data(self,**kwargs):
        context=super(Quien, self).get_context_data(**kwargs) 
        context['cursos']= Curso.objects.all()

        return context




"""
clase que maneja el login

--->Determinar plantilla de login:logrado
--->Determinar redireccionamiento en caso de un login valido:en_proceso
"""         
class Login_View(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('inicio')



class InfoCurso(DetailView):
    template_name = 'app/infocurso.html'
    model = Curso

    def get_context_data(self,**kwargs):
        context=super(InfoCurso, self).get_context_data(**kwargs)
        idCur = self.kwargs.get('pk',None)
        context['infocurso']= Curso.objects.get(pk = idCur)
        context['cursos']= Curso.objects.all()

  
        return context




"""
IMPORTANTE!!!
La funcionalidad del logout sera manejada por una clase 
que se definira en urls.py

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:inicio')
"""    
 


