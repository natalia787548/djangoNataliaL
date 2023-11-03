from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Pokoj(models.Model):
    numer_pokoju=models.IntegerField()
    typ_pokoju=models.ForeignKey('Typ_pokoju')
    class Meta:
        db_table= "Pokoj"
        verbose_name_plural = "Pokoj"

class Recepcja(models.Model):
    recepcja=models.CharField(max_length=1)
    class Meta:
        db_table= "Recepcja"
        verbose_name_plural = "Recepcja"

class Gosc_hotelowy(models.Model):
    imie=models.CharField(max_length=64)
    nazwisko=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    class Meta:
        db_table= "Gosc_hotelowy"
        verbose_name_plural = "Gosc_hotelowy"

class Hotel(models.Model):
    nazwa=models.CharField(max_lenght=200)
    adres=models.CharField(max_lenght=200)
    class Meta:
        db_table="Hotel"
        verbose_name_plural="Hotel"

class Typ_pokoju(models.Model):
    nazwa_typu_pokoju=models.CharField(max_lenght=150)
    ilosc_osob=models.IntegerField()
    cena=models.IntegerField()

    class Meta:
        db_table="Typ_pokoju"
        verbose_name_plural="Typ_pokoju"




