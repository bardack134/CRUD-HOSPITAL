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
    # logout()関数を使用してユーザーのセッションを終了します。
    logout(request)

    # Redirigimos al usuario a la página de inicio ('login' es el nombre de la URL).
    # ユーザーをホームページにリダイレクトします。
    return redirect('login')


#página de inicio de sesión
# ログインページ
def log(request):

    # Creamos una instancia del formulario de autenticación
    # ログインフォームのインスタンスを作成します
    form = AuthenticationForm()  
    
    context = {
        # Agregamos el formulario al contexto para pasarlo a la plantilla
         # フォームをコンテキストに追加してテンプレートに渡します
        'form': form  
    }

    
    # Renderizamos la plantilla "login.html" con el contexto proporcionado
    #コンテキストを "login.html" テンプレートをレンダリングします
    return render(request, 'login/login.html', context)   


# Creamos una vista basada en clase llamada LoginView, se usara para crear un formulario de login
# ログインフォームを作るためのクラス
class LoginView(View):  

    # Método GET para crear el formulario de inicio de sesión
    # GETメソッドでログインフォームを作成します
    def get(self, request):  
        
    #AuthenticationForm es una clase proporcionada por Django que se utiliza para crear un formulario de inicio de sesión en una aplicación web.

        # Creamos una instancia del formulario de inicio de session
        # ログインフォームのインスタンスを作成します
        form = AuthenticationForm() 

        # Preparamos el contexto con el formulario
        # フォームをコンテキストに追加してテンプレートに渡します
        context = {'form': form}  

        # Renderizamos la plantilla con el contexto
        #コンテキストを "login.html" テンプレートをレンダリングします
        return render(request, 'login/login.html', context)  

    # Método POST para procesar los datos del formulario
    def post(self, request):  # POSTメソッドでフォームデータを処理します

        # Creamos una instancia del formulario de inicio de session pero con los datos POST
         # データを持つ認証フォームのインスタンスを作成します
        form = AuthenticationForm(request, data=request.POST)  

        # Verificamos si el formulario es válido
        # フォームが正しいか確認します
        if form.is_valid():  
          
            # En Django, después de que los datos ingresados por el usuario se someten al proceso de validación, se almacenan en el atributo cleaned_data, cleaned_data es un diccionario y usamos el metodo get() para obtener el valor del campo username
            # ユーザーが入力したデータが確認された後、cleaned_dataに保存されます。cleaned_dataは辞書なので、get()メソッドでusernameフィールドの値を取得します。
            nombre_usuario = form.cleaned_data.get("username")  

            # Obtenemos la contraseña del formulario
            # usernameように、フォームからパスワードを取得します
            contra = form.cleaned_data.get("password") 

            # Autenticamos al usuario

            #authenticate() verifica si las credenciales proporcionadas son válidas y corresponden a un usuario en la base de datos. Si las credenciales son válidas, devuelve un objeto de usuario. Si no son válidas, devuelve None.
            # ユーザーを認証します。authenticate()は、入力された情報が正しいかどうかを確認し、正しければユーザーオブジェクトを返し、間違っていればNoneを返します。
            usuario = authenticate(username=nombre_usuario, password=contra) 

            # Si la autenticación fue exitosa
            # 認証が成功した場合
            if usuario is not None:  

                 # Iniciamos sesión para el usuario autenticado
                # 認証ユーザーのセッションを開始します
                login(request, usuario) 

                
                return redirect('RegistroPaciente')

            
            # Si la autenticación falló 
             # 認証に失敗した場合
            else:  

                # Mostramos un mensaje de error
                # エラーメッセージを表示します
                messages.error(request, "Usuario no válido")
                # return render(request, 'login/login.html') 
                
                return redirect('login')
             
        #フォームが正しくない場合
        else:  # Si el formulario no es válido
            messages.error(request, "You have entered an invalid username")  # Mostramos un mensaje de error
            
            return redirect('login')
        # #todo lo anterior ocurre si el usario hace el proceso de logear, si no hace le proceso de logear salta directamente a estas dos ultimas lineas

        # # Preparamos el contexto con el formulario (posiblemente con errores)
        # context = {'form': form}  

        # # Renderizamos la plantilla con el contexto
        # return render(request, 'login/login.html', context)  
        
        
        #TODO:REVISAR, ENTENDER, ESCR5IBIR COMENTARIOS EN  LA APP PATIENTES
        #TODO: REVISAR LOS COMENTARIOS ESCRITOS EN MODELS.PY Y FORMS.PY DE LA APP 'CRUD'
