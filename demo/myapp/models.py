from django.db import models

class PatientRecord(models.Model):
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	year = models.IntegerField()
	addr = models.CharField(max_length = 100)
	date = models.DateField(default='2024-01-01')
class MedicalReport(models.Model):
	name = models.CharField(max_length = 100, default = "")
	date = models.DateField(default='2024-01-01')
	symptoms = models.CharField(max_length=100)
	pred = models.CharField(max_length=100)
	medicine = models.CharField(max_length=100)
	amount = models.IntegerField()
	unit = models.CharField(max_length=100)
	way = models.CharField(max_length = 100)
class Bill(models.Model):
	name = models.CharField(max_length = 100, default = "")
	date = models.DateField(default='2024-01-01')
	cureCost = models.IntegerField()
	medicineCost = models.IntegerField()


