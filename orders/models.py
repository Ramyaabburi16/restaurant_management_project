from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
    