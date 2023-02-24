from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "client",
            "date_created",
            "date_updated",
            "support_contact",
            "event_status",
            "attendees",
            "event_date",
            "notes",
            "contract",
        ]
        read_only_fields = ["client", "contract"]

    def update(self, instance, validated_data):
        instance.support_contact = validated_data.get(
            "support_contact", instance.support_contact
        )
        instance.event_status = validated_data.get(
            "event_status", instance.event_status
        )
        instance.attendees = validated_data.get("attendees", instance.attendees)
        instance.event_date = validated_data.get("event_date", instance.event_date)
        instance.notes = validated_data.get("notes", instance.notes)

        if not instance.support_contact.groups.filter(name="support").exists():
            raise serializers.ValidationError(
                "Support_contact is not in group support!"
            )
        else:
            instance.save()
            return instance
