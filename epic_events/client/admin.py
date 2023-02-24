from django.contrib import admin

# Register your models here.
from client.models import Client, Contract

admin.site.register(Client)
admin.site.register(Contract)
