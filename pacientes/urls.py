from django.urls import path

#de las vistas importamos las clases que creamos
from .views import lista_pacientes, patient_list, patient_listJP


urlpatterns = [
    # Asignamos la vista RegisterView a la URL raiz, con el nombre 'autenticacion'.
    path('', lista_pacientes, name='lista_pacientes'),

    path('en', patient_list, name='patient_list'),

    path('jp', patient_listJP, name='patient_listJP'),
    


]
