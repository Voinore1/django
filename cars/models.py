from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.TextField(max_length=100)
    model = models.TextField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.URLField()

    def __str__(self):
        return self.make + ' ' + self.model + ' ' + '$' + self.price