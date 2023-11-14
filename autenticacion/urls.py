from django.urls import path

#de las vistas importamos las clases que creamos
from .views import  LoginView, cerrar_sesion


urlpatterns = [


    # Asignamos la función 'cerrar_sesion' a la URL 'cerrar/', con el nombre 'cerrar_sesion'.
    path('cerrar/', cerrar_sesion, name='cerrar_sesion'),

    path('', LoginView.as_view(), name='login'),
]


    

