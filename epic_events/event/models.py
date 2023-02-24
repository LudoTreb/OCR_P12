from django.conf import settings
from django.db import models

# Create your models here.
from client.models import Client, Contract


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    event_status = models.BooleanField(default=False)
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.client} {self.support_contact}"

    class Meta:
        ordering = ['-event_date']