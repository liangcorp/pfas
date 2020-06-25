import investments.constants as constants

from django.db import models


# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_description = models.CharField(max_length=30)
    stock_security = models.CharField(max_length=10)

    stock_initial_share = models.DecimalField(
        max_digits=constants.SHARE_MAX_DIGITS,
        decimal_places=constants.SHARE_DECIMAL_PLACES)

    stock_initial_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    stock_current_share = models.DecimalField(
        max_digits=constants.SHARE_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    stock_current_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.SHARE_DECIMAL_PLACES)

    def get_stock_name(self):
        return self.stock_name

    def get_stock_current_stock(self):
        return self.stock_current_stock


class StockTransaction(models.Model):
    transaction_date = models.DateField(
        (""), auto_now=True, auto_now_add=False)

    transaction_description = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH)

    transaction_category = models.CharField()

    transaction_shares = models.DecimalField(
        max_digits=constants.SHARE_MAX_DIGITS,
        decimal_places=constants.SHARE_DECIMAL_PLACES)

    transaction_fee = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_price_each = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_price_total = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    tranaction_reconciled = models.BooleanField(default=False)
