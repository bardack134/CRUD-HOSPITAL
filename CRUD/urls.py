from django.urls import path

#de las vistas importamos las clases que creamos
from .views import RegisterPatient, RegisterPatientSP, RegisterPatientJP


urlpatterns = [
    # Asignamos la vista RegisterView a la URL raiz, con el nombre 'autenticacion'.
    
    path('', RegisterPatient.as_view(), name='RegisterPatient'),
    path('sp/', RegisterPatientSP.as_view(), name='RegistroPaciente'),
    path('jp/', RegisterPatientJP.as_view(), name='RegistroPacienteJP'),


]
