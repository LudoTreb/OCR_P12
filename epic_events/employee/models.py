from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        group_name = str(self.groups.first())
        return f"{self.first_name} {self.last_name} {group_name.capitalize()}"
