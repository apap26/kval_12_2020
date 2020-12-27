from django.db import models


# Create your models here.
class drivers(models.Model):
    name = models.CharField(max_length=200)
    familia = models.CharField(max_length=200)
    otchestvo = models.CharField(max_length=200)
    license_number = models.CharField(max_length=10)


class cars_brand(models.Model):
    name = models.CharField(max_length=100)


class cars(models.Model):
    cars_brand = models.ForeignKey(cars_brand, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=8)
    insurance_number = models.CharField(max_length=100)


class type_incident(models.Model):
    name = models.CharField(max_length=220)


class conditionals(models.Model):
    name = models.CharField(max_length=100)


class reasons_DTP(models.Model):
    name = models.CharField(max_length=228)


class cards(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=500)
    incident = models.ForeignKey(type_incident, on_delete=models.CASCADE)
    driver = models.ForeignKey(drivers, on_delete=models.CASCADE)
    died_count = models.IntegerField()
    injured_count = models.IntegerField()
    car = models.ForeignKey(cars, on_delete=models.CASCADE)
    Погода = models.ForeignKey(conditionals, on_delete=models.CASCADE)
    Причины = models.ManyToManyField(reasons_DTP)