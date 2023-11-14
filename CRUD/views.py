# Importamos los elementos necesarios de Django para manejar los formularios y la vista.
from django.contrib.auth import forms
from django.shortcuts import redirect, render

# Importamos el módulo para manejar mensajes
from django.contrib import messages

from django.views.generic import View

from .forms_jp import PatientInformationFormJP


# Importamos el formulario personalizado.
from .forms_en import PatientInformationForm 

from .forms_sp import PatientInformationFormSP

#TemplateView ya está diseñada para renderizar una plantilla específica cuando se accede a la vista. Aquí, template_name se establece en 'registro/gracias.html', lo que significa que cuando se acceda a esta vista, se renderizará la plantilla gracias.html.
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Creamos una vista basada en clase (VBC) llamada RegisterView que hereda de View.
@method_decorator(login_required, name='dispatch')
class RegisterPatient(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        # Creamos una instancia del formulario personalizado.
        form = PatientInformationForm()  

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'form': form 
        }

        # Mostramos la página de registro con el formulario.
        return render(request, 'registro/register.html', context) 


    # Método POST para procesar los datos del formulario cuando se envía.
    def post(self, request):
        

        # Creamos una instancia del formulario con los datos del POST.
        form = PatientInformationForm(request.POST)  

        # Verificamos si los datos ingresados en el formulario son válidos.
        if form.is_valid():

          
            """
            #para que el usuario logee automaticamente
            usuario=form.save()
            login(request, usuario)
            """
            # Guarda el formulario en la base de datos
            patient = form.save()  # Esto guarda los datos en la base de datos y devuelve el objeto creado


            # Mostramos un mensaje de éxito.
            messages.success(request, 'Patient registered successfully.')  

             # Redirige a la misma vista de registro
            return redirect('RegisterPatient')
 

        context = {
            # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
            'form': form  
        }

        #Mostramos la página de registro con el formulario y posibles errores.
        return render(request, 'registro/register.html', context)  



#@login_required(login_url='/autenticacion/login/')
@method_decorator(login_required, name='dispatch')
class RegisterPatientSP(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        # Creamos una instancia del formulario personalizado.
        form = PatientInformationFormSP()

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'formSP': form 
        }

        # Mostramos la página de registro con el formulario.
        return render(request, 'registro/registro.html', context) 


    def post(self, request):
        

        # Creamos una instancia del formulario con los datos del POST.
        form = PatientInformationFormSP(request.POST)  

        # Verificamos si los datos ingresados en el formulario son válidos.
        if form.is_valid():

          
            """
            #para que el usuario logee automaticamente
            usuario=form.save()
            login(request, usuario)
            """
            # Guarda el formulario en la base de datos
            patient = form.save()  # Esto guarda los datos en la base de datos y devuelve el objeto creado


            # Mostramos un mensaje de éxito.
            messages.success(request, 'Paciente registrado exitosamente.')  

             # Redirige a la misma vista de registro
            return redirect('RegistroPaciente')  

        context = {
            # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
            'form': form  
        }

        #Mostramos la página de registro con el formulario y posibles errores.
        return render(request, 'registro/registro.html', context)  

#@login_required(login_url='/autenticacion/login/')
@method_decorator(login_required, name='dispatch')
class RegisterPatientJP(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        # Creamos una instancia del formulario personalizado.
        form = PatientInformationFormJP()

        # Preparamos los datos del formulario para pasar al contexto.
        context = {
            'formJP': form 
        }

        # Mostramos la página de registro con el formulario.
        return render(request, 'registro/registerJP.html', context) 


    # Método POST para procesar los datos del formulario cuando se envía.
    def post(self, request):
        

        # Creamos una instancia del formulario con los datos del POST.
        form = PatientInformationFormJP(request.POST)  

        # Verificamos si los datos ingresados en el formulario son válidos.
        if form.is_valid():

          
            """
            #para que el usuario logee automaticamente
            usuario=form.save()
            login(request, usuario)
            """
            # Guarda el formulario en la base de datos
            patient = form.save()  # Esto guarda los datos en la base de datos y devuelve el objeto creado


            # Mostramos un mensaje de éxito.
            messages.success(request, '患者は正常に登録されました。')  

             # Redirige a la misma vista de registro
            return redirect('RegistroPacienteJP')  

        context = {
            # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
            'form': form  
        }

        #Mostramos la página de registro con el formulario y posibles errores.
        return render(request, 'registro/registerJP.html', context)  
        