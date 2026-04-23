from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Campo para saber se é funcionário da cafeteria
    is_coffee_staff = models.BooleanField(default=False)
    # Campo para telefone (útil para avisar que o café está pronto!)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username