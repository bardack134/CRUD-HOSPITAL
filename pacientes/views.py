# Importa la función 'render' desde el módulo 'shortcuts' de Django
from django.shortcuts import render
# Importa el modelo 'PatientInformation' desde el archivo 'models.py' de la aplicación 'CRUD'
from CRUD.models import PatientInformation
from CRUD.modelsJP import PatientInformationJP
from CRUD.modelsSP import PatientInformationSP



# Define una vista llamada 'lista_pacientes' que toma un objeto 'request' como parámetro
def lista_pacientes(request):
    
    # Obtiene todos los objetos (registros) de la base de datos correspondientes al modelo 'PatientInformation'
    patients = PatientInformationSP.objects.all()

    # Obtén los parámetros de búsqueda del GET request
    search_date = request.GET.get('search_date')
    search_name = request.GET.get('search_name')

    # Aplica filtros si se proporcionan parámetros de búsqueda
    if search_date:
        patients = patients.filter(date__icontains=search_date)
    if search_name:
        patients = patients.filter(name__icontains=search_name)

        
    # Utiliza la función 'render' para renderizar la plantilla 'lista_pacientes.html' con los datos de los pacientes
    # Pasa el objeto 'request', el nombre de la plantilla y un diccionario con los datos a la plantilla
    # Los datos de los pacientes se pasan al diccionario bajo la clave 'patients'
    return render(request, 'pacientes/lista_pacientes.html', {'patients': patients})


# Define una vista llamada 'patient_list' que toma un objeto 'request' como parámetro
def patient_list(request):
    
    # Obtiene todos los objetos (registros) de la base de datos correspondientes al modelo 'PatientInformation'
    patients = PatientInformation.objects.all()

    # Obtén los parámetros de búsqueda del GET request
    search_date = request.GET.get('search_date')
    search_name = request.GET.get('search_name')

    # Aplica filtros si se proporcionan parámetros de búsqueda
    if search_date:
        patients = patients.filter(date__icontains=search_date)
    if search_name:
        patients = patients.filter(name__icontains=search_name)

    # Utiliza la función 'render' para renderizar la plantilla 'lista_pacientes.html' con los datos de los pacientes
    # Pasa el objeto 'request', el nombre de la plantilla y un diccionario con los datos a la plantilla
    # Los datos de los pacientes se pasan al diccionario bajo la clave 'patients'
    return render(request, 'pacientes/patients.html', {'patients': patients})



# Define una vista llamada 'patient_listJP' que toma un objeto 'request' como parámetro
def patient_listJP(request):
    
    # Obtiene todos los objetos (registros) de la base de datos correspondientes al modelo 'PatientInformation'
    patients = PatientInformationJP.objects.all()

    # Obtén los parámetros de búsqueda del GET request
    search_date = request.GET.get('search_date')
    search_name = request.GET.get('search_name')

    # Aplica filtros si se proporcionan parámetros de búsqueda
    if search_date:
        patients = patients.filter(date__icontains=search_date)
    if search_name:
        patients = patients.filter(name__icontains=search_name)


    # Utiliza la función 'render' para renderizar la plantilla 'lista_pacientes.html' con los datos de los pacientes
    # Pasa el objeto 'request', el nombre de la plantilla y un diccionario con los datos a la plantilla
    # Los datos de los pacientes se pasan al diccionario bajo la clave 'patients'
    return render(request, 'pacientes/patientsJP.html', {'patients': patients})