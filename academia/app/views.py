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




         
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('app:curso')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:inicio')
 


