from django.db import models


# Create your models here.
class Income(models.Model):
    income_name = models.CharField(max_length=20)
    income_balance = models.DecimalField(
        max_digits=19, decimal_places=2)
    income_total = models.DecimalField(
        max_digits=19, decimal_places=2)


def get_income_name(self):
    return self.income_name


def get_income_balance(self):
    return self.income_balance


def get_income_total(self):
    return self.income_total
