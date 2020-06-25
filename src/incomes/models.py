import incomes.constants as constants

from django.db import models


# Create your models here.
class Income(models.Model):
    income_name = models.CharField(max_length=20)
    income_balance = models.DecimalField(
        max_digits=19, decimal_places=2)
    income_total = models.DecimalField(
        max_digits=19, decimal_places=2)
    income_currency = models.CharField(max_length=10)


def get_income_name(self):
    return self.income_name


def get_income_balance(self):
    return self.income_balance


def get_income_total(self):
    return self.income_total


def get_income_currency(self):
    return self.income_currency


class IncomeTransaction(models.Model):
    transaction_date = models.DateField(
        (""), auto_now=True, auto_now_add=False)

    transaction_description = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH)

    transaction_category = models.CharField()

    transaction_charge = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_income = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_result_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    tranaction_reconciled = models.BooleanField(default=False)
