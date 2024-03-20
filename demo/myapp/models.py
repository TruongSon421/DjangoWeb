from django.db import models

class PatientRecord(models.Model):
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	year = models.IntegerField()
	addr = models.CharField(max_length = 100)
	date = models.DateField(default='2024-01-01')
class MedicalReport(models.Model):
	patient = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
	symptoms = models.CharField(max_length=100)
	pred = models.CharField(max_length=100)
	medicine = models.CharField(max_length=100)
	UNIT_CHOICES = [
	    ('viên', 'Viên'),
        ('chai', 'Chai'),
    ]
	unit = models.CharField(max_length=4, choices=UNIT_CHOICES)
    
	WAY_CHOICES = [
        (1, 'Cách 1'),
        (2, 'Cách 2'),
        (3, 'Cách 3'),
        (4, 'Cách 4'),
    ]
	way = models.IntegerField(choices=WAY_CHOICES)

