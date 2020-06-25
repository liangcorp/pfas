from django.db import models


# Create your models here.
class Liability(models.Model):
    liability_name = models.CharField(max_length=20)
    liability_balance = models.DecimalField(
        max_digits=19, decimal_places=2)
    liability_total = models.DecimalField(
        max_digits=19, decimal_places=2)
    liability_currency = models.CharField(max_length=10)


def get_liability_name(self):
    return self.liability_name


def get_liability_balance(self):
    return self.liability_balance


def get_liability_total(self):
    return self.liability_total


def get_liability_currency(self):
    return self.liability_currency
