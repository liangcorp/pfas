import assets.constants as constants

from django.db import models


# Create your models here.
class Asset(models.Model):
    CASH = 'CASH'
    BANK = 'BANK'
    ASSET = 'ASSET'

    CATEGORY_CHOICES = [
        (CASH, 'Cash'),
        (BANK, 'Bank'),
        (ASSET, 'Asset'),
    ]

    asset_name = models.CharField(max_length=20)
    asset_description = models.CharField(max_length=30)
    asset_currency = models.CharField(max_length=10)

    asset_initial_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    asset_current_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    asset_open_date = models.DateField('opening date')

    asset_type = models.CharField(
        max_length=6,
        choices=CATEGORY_CHOICES,
        default=BANK,
    )

    def get_asset_name(self):
        return self.asset_name

    def get_asset_current_balance(self):
        return self.asset_current_balance


class AssetTransaction(models.Model):
    transaction_date = models.DateField(
        (""), auto_now=True, auto_now_add=False)

    transaction_description = models.CharField(
        max_length=constants.DESCRIPTION_MAX_LENGTH)

    transaction_category = models.CharField()

    transaction_deposit = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_withdraw = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    transaction_result_balance = models.DecimalField(
        max_digits=constants.CASH_MAX_DIGITS,
        decimal_places=constants.CASH_DECIMAL_PLACES)

    tranaction_reconciled = models.BooleanField(default=False)
