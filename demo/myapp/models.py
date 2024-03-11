from django.db import models

class PatientRecord(models.Model):
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	year = models.IntegerField()
	addr = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
#class MedicalReport(models.Model):
