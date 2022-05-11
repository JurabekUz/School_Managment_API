from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    first_name = None
    last_name = None

    def __str__(self):
        return self.username

