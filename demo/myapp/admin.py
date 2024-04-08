from django.contrib import admin
from .models import PatientRecord,MedicalReport
# Register your models here.
admin.site.register(PatientRecord)
admin.site.register(MedicalReport)