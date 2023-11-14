from django.contrib import admin
from .models import PatientInformation   # Importamos el modelo PatientInformation desde el archivo models.py de la misma carpeta
from .modelsSP import PatientInformationSP 
from .modelsJP import PatientInformationJP 
# Define la configuración del administrador para el modelo PatientInformation
class PatientInformationAdmin(admin.ModelAdmin):

    

    list_display=("category_registration", "date", "updated",  "hospital_ward", "room", "patient_code", "name", "gender", "admitting_department", "outcome", "admitting_physician", "diagnosis",)

    # Establece los campos 'created' y 'updated' como campos de solo lectura en la interfaz de administración
    readonly_fields = ('date', 'updated')

# Registra el modelo PatientInformation con su configuración personalizada en la interfaz de administración
admin.site.register(PatientInformation, PatientInformationAdmin)


# Define la configuración del administrador para el modelo PatientInformationSP
class PatientInformationSPAdmin(admin.ModelAdmin):

    

    list_display=("category_registration", "date", "updated",  "hospital_ward", "room", "patient_code", "name", "gender", "admitting_department", "outcome", "admitting_physician", "diagnosis",)

    # Establece los campos 'created' y 'updated' como campos de solo lectura en la interfaz de administración
    readonly_fields = ('date', 'updated')

# Registra el modelo PatientInformation con su configuración personalizada en la interfaz de administración
admin.site.register(PatientInformationSP, PatientInformationSPAdmin)

# Define la configuración del administrador para el modelo PatientInformationSP
class PatientInformationJPAdmin(admin.ModelAdmin):

    

    list_display=("category_registration", "date", "updated",  "hospital_ward", "room", "patient_code", "name", "gender", "admitting_department", "outcome", "admitting_physician", "diagnosis",)

    # Establece los campos 'created' y 'updated' como campos de solo lectura en la interfaz de administración
    readonly_fields = ('date', 'updated')

# Registra el modelo PatientInformation con su configuración personalizada en la interfaz de administración
admin.site.register(PatientInformationJP, PatientInformationJPAdmin)