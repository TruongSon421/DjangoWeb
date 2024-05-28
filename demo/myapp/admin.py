from django.contrib import admin
from .models import PatientList, MedicalExamination, Patient,MedicationStockList,MedicationUsageReport,DetailedPatientList
# Register your models here.
admin.site.register(PatientList)
admin.site.register(MedicalExamination)
admin.site.register(Patient)
admin.site.register(MedicationStockList)
admin.site.register(MedicationUsageReport)
admin.site.register(DetailedPatientList)