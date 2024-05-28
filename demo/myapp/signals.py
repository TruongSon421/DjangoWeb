from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MedicalExamination, MedicationUsageReport

@receiver(post_save, sender=MedicalExamination)
def update_medication_usage_report(sender, instance, created, **kwargs):
    if created:
        MedicationUsageReport.update_usage_count(instance.med.medication_name, instance.num_med)
