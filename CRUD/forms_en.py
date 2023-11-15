from django import forms  # Importamos el módulo 'forms' de Django

from .models import PatientInformation  # Importamos el modelo 'PatientInformation' desde el archivo 'models.py' en la misma carpeta

# Definición de la clase del formulario para 'PatientInformation'
class PatientInformationForm(forms.ModelForm):  
    class Meta:  
        model = PatientInformation  # Asociamos el formulario con el modelo 'PatientInformation'
        fields = "__all__"  # Incluimos todos los campos del modelo en el formulario

# En esta clase se define un formulario de Django basado en el modelo 'PatientInformation'.
# El formulario contendrá todos los campos definidos en el modelo y será fácil de usar para crear o actualizar instancias del modelo.
