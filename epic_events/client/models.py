from django.conf import settings
from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contract(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.SET_NULL, blank=True, null=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_signed = models.BooleanField(default=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Client is: {self.client} with {self.sales_contact}"
