import expenses.contants as constants

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


class ExpenseTransaction(models.Model):
    transaction_date = models.DateField(
        (""), auto_now=True, auto_now_add=False)

    transaction_description = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH)

    transaction_category = models.CharField()

    transaction_expense = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_rebate = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_result_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    tranaction_reconciled = models.BooleanField(default=False)
