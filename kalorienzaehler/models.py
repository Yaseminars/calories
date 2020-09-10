from django.db import models
from django.utils import timezone

class Nutzer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    maxCalories = models.IntegerField(null=True)
    def __str__(self):
        return self.username

class usedCalories(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    Mahlzeit = models.CharField(max_length=50)
    user = models.ForeignKey(Nutzer, null=True, on_delete=models.CASCADE)
    Kilokalorien = models.IntegerField()
    def __str__(self):
        return self.Mahlzeit + ", " + str(self.Kilokalorien) + ", " + str(self.user.username)
