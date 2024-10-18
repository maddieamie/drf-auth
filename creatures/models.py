from django.db import models
from django.contrib.auth.models import User

class MagicalCreature(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    magical_power = models.CharField(max_length=100)
    description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
