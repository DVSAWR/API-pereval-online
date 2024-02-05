from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=64, default=None)
    name = models.CharField(max_length=64, default=None)
    patronymic = models.CharField(max_length=64, default=None)
    email = models.EmailField(unique=True, default=None)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class Coords(models.Model):
    ...