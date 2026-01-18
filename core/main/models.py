from django.db import models

class Car(models.Model):
    car_model = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.car_model


# Create your models here.
