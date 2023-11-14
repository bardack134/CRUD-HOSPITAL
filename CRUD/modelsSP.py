from django.db import models

# Definición del modelo PatientInformation
class PatientInformationSP(models.Model):
    # Campo para la categoría de registro del paciente
    category_registration = models.CharField(max_length=100)
    
    # Campo para la fecha de creación (se actualiza automáticamente)
    date = models.DateTimeField(auto_now_add=True)
    
    # Campo para la fecha de actualización (se actualiza automáticamente)
    updated = models.DateTimeField(auto_now=True)
    
    # Campo para el ala del hospital
    hospital_ward = models.CharField(max_length=10)
    
    # Campo para el número de la habitación (números enteros positivos)
    room = models.PositiveIntegerField()
    
    # Campo para el código del paciente (números enteros positivos)
    patient_code = models.PositiveIntegerField()
    
    # Campo para el nombre del paciente
    name = models.CharField(max_length=100)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    # Campo para el género del paciente con las opciones definidas
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Campo para el departamento de admisión del paciente
    admitting_department = models.CharField(max_length=20)
    
    # Campo para el resultado o desenlace del paciente
    outcome = models.CharField(max_length=100)
    
    # Campo para el médico responsable de la admisión del paciente
    admitting_physician = models.CharField(max_length=50)
    
    # Campo para el diagnóstico del paciente
    diagnosis = models.CharField(max_length=100)

    # Configuración adicional del modelo
    class Meta:
        verbose_name = 'Información del Paciente'  # Nombre singular para la interfaz administrativa

        verbose_name_plural = 'Información de los Pacientes'  # Nombre plural para la interfaz administrativa

    # Método para devolver una representación legible del modelo
    def __str__(self):
        return self.name
