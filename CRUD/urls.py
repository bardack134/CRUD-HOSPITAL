from django.urls import path

#de las vistas importamos las clases que creamos
# views から作成したクラスをインポートします
from .views import RegisterPatient, RegisterPatientSP, RegisterPatientJP


urlpatterns = [
    # Asignamos la vista RegisterView a la URL raiz, con el nombre 'autenticacion'.
    # ルートURLにviewに書いてあるクラスを設定します
    path('', RegisterPatient.as_view(), name='RegisterPatient'),
    path('sp/', RegisterPatientSP.as_view(), name='RegistroPaciente'),
    path('jp/', RegisterPatientJP.as_view(), name='RegistroPacienteJP'),


]
