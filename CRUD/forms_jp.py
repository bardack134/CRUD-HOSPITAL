from django import forms
from .modelsJP import PatientInformationJP

# Definición de la clase del formulario para 'PatientInformation'
class PatientInformationFormJP(forms.ModelForm):
    # Cambia los nombres de los campos en el formulario
    category_registration = forms.CharField(label="登録区分", max_length=100)

    
    
    hospital_ward = forms.CharField(label="病棟 ", max_length=10)
    
    room = forms.IntegerField(label="部屋")
    
    patient_code = forms.IntegerField(label="患者コ・ド")
    
    name = forms.CharField(label="名前", max_length=100)
   
    GENDER_CHOICES = [
         ('', '選択してください'),
        ('M', '男性'),
        ('F', '女性'),
    ]

    gender = forms.ChoiceField(label="性別", choices=GENDER_CHOICES)
    
   
    admitting_department = forms.CharField(label="入院診療科", max_length=20)
   
    outcome = forms.CharField(label="転帰", max_length=100)
    
    admitting_physician = forms.CharField(label="入院主治医", max_length=50)
   
    diagnosis = forms.CharField(label="病名", max_length=100)
    
    class Meta:
        model = PatientInformationJP
        fields = "__all__"
