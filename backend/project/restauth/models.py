from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuPairUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)

