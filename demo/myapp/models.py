from django.db import models

class PatientRecord(models.Model):
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	year = models.IntegerField()
	addr = models.CharField(max_length = 100)
	date = models.DateField(default='2024-01-01')
#class MedicalReport(models.Model):
