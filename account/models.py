from django.db import models
from django.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADDE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
 