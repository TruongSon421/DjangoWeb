# models.py
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
UNIT_CHOICES = (
    ("vien", "Viên"),
    ("chai", "Chai"),
)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birth_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )
    address = models.CharField(max_length=255)

class PatientList(models.Model):
    MAX_PATIENTS_PER_DAY = 40
    date = models.DateField(default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    @classmethod
    def can_add_patient(cls, date):
        count = cls.objects.filter(date=date).count()
        return count < cls.MAX_PATIENTS_PER_DAY

DISEASE_CHOICE = (
    ("benh_1", "Bệnh 1"),
    ("benh_2", "Bệnh 2"),
    ("benh_3", "Bệnh 3"),
    ("benh_4", "Bệnh 4"),
    ("benh_5", "Bệnh 5"),
)
class MedicationStockList(models.Model):
    medication_name = models.CharField(max_length=255)
    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default="vien",
    )
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    date_added = models.DateField(default=timezone.now)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class MedicalExamination(models.Model):
    patientlist = models.ForeignKey(PatientList, on_delete=models.CASCADE)
    symptoms = models.TextField()
    disease_prediction = models.CharField(
        max_length=255,
        choices=DISEASE_CHOICE,
        default="benh_1",
    )
    med = models.ForeignKey(MedicationStockList,on_delete=models.CASCADE)
    num_med = models.IntegerField()

class DetailedPatientList(models.Model):
    patientlist = models.ForeignKey(PatientList, on_delete=models.CASCADE)
    examination = models.ForeignKey(MedicalExamination, on_delete=models.CASCADE)

class MedicationUsageReport(models.Model):
    month = models.DateField()
    medication_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
