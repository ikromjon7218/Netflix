from django.db import models
from django.core.validators import MinValueValidator
# from django.core.exeptions import ValidationError
from django.contrib.auth.models import User

class Aktyor(models.Model):
    ism = models.CharField(max_length=100)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=10)
    davlat = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.ism}"

class Kino(models.Model):
    nom = models.CharField(max_length=1000)
    yil = models.DateField()
    janr = models.CharField(max_length=100)
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self):
        return f"{self.nom}"

class Tarif(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.PositiveIntegerField()
    muddat = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nom}"

class Izoh(models.Model):
    izoh = models.CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    sana = models.DateField()