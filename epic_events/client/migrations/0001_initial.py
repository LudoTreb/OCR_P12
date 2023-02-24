# Generated by Django 4.1.7 on 2023-02-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254, verbose_name=100)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("mobile", models.CharField(blank=True, max_length=20, null=True)),
                ("company_name", models.CharField(max_length=25)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
                ("is_signed", models.BooleanField(default=True)),
                ("amount", models.FloatField(blank=True, null=True)),
                ("payment_due", models.DateField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="client.client",
                    ),
                ),
            ],
        ),
    ]
