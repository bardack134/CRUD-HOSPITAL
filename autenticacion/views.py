from django.shortcuts import redirect, render


#AuthenticationForm es una clase proporcionada por Django que se utiliza para crear un formulario de inicio de sesión en una aplicación web.
# AuthenticationFormはDjangoのクラスです、ログインフォームを作るために使います"
from django.contrib.auth.forms import  AuthenticationForm

from django.views.generic import View

from django.contrib.auth import login, logout, authenticate


# Importamos el módulo para manejar mensajes<
# メッセージを処理するためのモジュール
from django.contrib import messages


def cerrar_sesion(request):
    # Utilizamos la función logout() para cerrar la sesión del usuario.
    logout(request)

    # Redirigimos al usuario a la página de inicio ('home' es el nombre de la URL).
    return redirect('login')


#página de inicio de sesión
def log(request):

    # Creamos una instancia del formulario de autenticación
    form = AuthenticationForm()  
    
    context = {
        # Agregamos el formulario al contexto para pasarlo a la plantilla
        'form': form  
    }

    
    # Renderizamos la plantilla "login.html" con el contexto proporcionado
    return render(request, 'login/login.html', context)   


# Creamos una vista basada en clase llamada LoginView, se usara para crear un formulario de login
class LoginView(View):  

    # Método GET para crear el formulario de inicio de sesión
    def get(self, request):  
        
    #AuthenticationForm es una clase proporcionada por Django que se utiliza para crear un formulario de inicio de sesión en una aplicación web.

        # Creamos una instancia del formulario de inicio de session
        form = AuthenticationForm() 

        # Preparamos el contexto con el formulario
        context = {'form': form}  

        # Renderizamos la plantilla con el contexto
        return render(request, 'login/login.html', context)  

    # Método POST para procesar los datos del formulario
    def post(self, request):  

        # Creamos una instancia del formulario de inicio de session pero con los datos POST
        form = AuthenticationForm(request, data=request.POST)  

        # Verificamos si el formulario es válido
        if form.is_valid():  

            

            # En Django, después de que los datos ingresados por el usuario se someten al proceso de validación, se almacenan en el atributo cleaned_data, cleaned_data es un diccionario y usamos el metodo get() para obtener el valor del campo username
            nombre_usuario = form.cleaned_data.get("username")  

            # Obtenemos la contraseña del formulario
            contra = form.cleaned_data.get("password") 

            # Autenticamos al usuario

            #authenticate() verifica si las credenciales proporcionadas son válidas y corresponden a un usuario en la base de datos. Si las credenciales son válidas, devuelve un objeto de usuario. Si no son válidas, devuelve None.
            usuario = authenticate(username=nombre_usuario, password=contra) 

            # Si la autenticación fue exitosa
            if usuario is not None:  

                 # Iniciamos sesión para el usuario autenticado
                login(request, usuario) 

                
                return redirect('RegistroPaciente')

            
            # Si la autenticación falló 
            else:  

                # Mostramos un mensaje de error
                messages.error(request, "Usuario no válido")

        else:  # Si el formulario no es válido
            messages.error(request, "Información incorrecta")  # Mostramos un mensaje de error

        #todo lo anterior ocurre si el usario hace el proceso de logear, si no hace le proceso de logear salta directamente a estas dos ultimas lineas

        # Preparamos el contexto con el formulario (posiblemente con errores)
        context = {'form': form}  

        # Renderizamos la plantilla con el contexto
        return render(request, 'login/login.html', context)  
