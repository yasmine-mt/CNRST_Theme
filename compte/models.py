from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=[('gestionnaire', 'Gestionnaire'), ('administrateur','Administrateur'),('visiteur', 'Visiteur')], default='visiteur')


