from django.db import models


# Create your models here.
class Expense(models.Model):
    expense_name = models.CharField(max_length=20)
    expense_balance = models.DecimalField(
        max_digits=19, decimal_places=2)
    expense_total = models.DecimalField(
        max_digits=19, decimal_places=2)
    expense_currency = models.CharField(max_length=10)


def get_expense_name(self):
    return self.expense_name


def get_expense_balance(self):
    return self.expense_balance


def get_expense_total(self):
    return self.expense_total


def get_expense_currency(self):
    return self.expense_currency
