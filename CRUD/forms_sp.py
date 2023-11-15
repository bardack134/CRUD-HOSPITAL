from django import forms


from .modelsSP import PatientInformationSP

# Definición de la clase del formulario para 'PatientInformation'
class PatientInformationFormSP(forms.ModelForm):
    
    # Cambia los nombres de los campos en el formulario
    category_registration = forms.CharField(label="Categoría de registro", max_length=100)
    """
    date = forms.DateTimeField(label="Fecha", widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
   
    updated = forms.DateTimeField(label="Ultima actualizacion", widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))
    """
    
    hospital_ward = forms.CharField(label="pabellon del hospital", max_length=10)
    
    room = forms.IntegerField(label="Numero de cuarto")
    
    patient_code = forms.IntegerField(label="Codigo del paciente")
    
    name = forms.CharField(label="Nombre completo", max_length=100)
    
    GENDER_CHOICES = [
         ('', 'Seleccione'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    gender = forms.ChoiceField(label="Genero", choices=GENDER_CHOICES)
   
    admitting_department = forms.CharField(label="Departamento de admision", max_length=20)
   
    outcome = forms.CharField(label="Resultado", max_length=100)
    
    admitting_physician = forms.CharField(label="Medico responsable de la admision", max_length=50)
   
    diagnosis = forms.CharField(label="Diagnostico medico", max_length=100)
    
    class Meta:
        model = PatientInformationSP
        fields = "__all__"
