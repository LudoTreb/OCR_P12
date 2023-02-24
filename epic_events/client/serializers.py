from rest_framework import serializers

from client.models import Client, Contract
from event.models import Event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
            "date_created",
            "date_updated",
            "sales_contact",
        ]

    def validate_sales_contact(self, sales_contact):
        if not sales_contact.groups.filter(name="sales").exists():
            raise serializers.ValidationError("Sales_contact is not in group sales.")
        else:
            return sales_contact

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "client",
            "sales_contact",
            "date_created",
            "date_updated",
            "is_signed",
            "amount",
            "payment_due",
        ]

    def validate_sales_contact(self, sales_contact):
        if not sales_contact.groups.filter(name="sales").exists():
            raise serializers.ValidationError("Sales_contact is not in group sales.")
        else:
            return sales_contact

    def create(self, validated_data):
        contract = Contract.objects.create(**validated_data)
        event = Event.objects.create(contract=contract, client=contract.client)
        contract.save()
        event.save()
        return contract

    def update(self, instance, validated_data):
        validated_data.pop("client", None)
        return super().update(instance, validated_data)
