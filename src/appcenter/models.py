from django.db import models
from django.contrib.auth.models import User


"""
 AppCenter model controls all models that relates to the app
 Other app related models reports to it.
"""

"""
class AppCenter(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="appcenter",
                             null=True)
"""


# Create your models here.
class Category(models.Model):
    ASSETS = 'ASSETS'
    EXPENSES = 'EXPENSES'
    INCOMES = 'INCOMES'
    LIABILITIES = 'LIABILITIES'

    CATEGORY_CHOICES = [
        (ASSETS, 'Assets'),
        (EXPENSES, 'Expenses'),
        (INCOMES, 'Incomes'),
        (LIABILITIES, 'Liabilities'),
    ]
    account_category = models.CharField(
        max_length=12,
        choices=CATEGORY_CHOICES,
        default=ASSETS,
    )


class Asset(models.Model):
    asset_name = models.CharField(max_length=10)
    asset_description = models.CharField(max_length=50)
    asset_currency = models.CharField(max_length=10)
    asset_type = models.CharField(max_length=10)
    asset_initial_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
    asset_current_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
    asset_open_date = models.DateField('opening date')


class AssetType(models.Model):
    CASH = 'CASH'
    BANK = 'BANK'
    STOCK = 'STOCK'
    ASSET = 'ASSET'

    CATEGORY_CHOICES = [
        (CASH, 'Cash'),
        (BANK, 'Bank'),
        (STOCK, 'Stock'),
        (ASSET, 'Asset'),
    ]
    account_category = models.CharField(
        max_length=6,
        choices=CATEGORY_CHOICES,
        default=BANK,
    )


class Liability(models.Model):
    liability_name = models.CharField(max_length=10)
    liability_description = models.CharField(max_length=50)
    liability_currency = models.CharField(max_length=10)
    liability_type = models.CharField(max_length=10)
    liability_initial_balance = models.DecimalField(max_digits=19,
                                                    decimal_places=2)
    liability_current_balance = models.DecimalField(max_digits=19,
                                                    decimal_places=2)
    liability_open_date = models.DateField('opening date')


class Stock(models.Model):
    stock_name = models.CharField(max_length=15)
    stock_description = models.CharField(max_length=50)
    stock_currency = models.CharField(max_length=10)
    stock_security = models.CharField(max_length=10)
    stock_initial_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
    stock_current_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
    stock_open_date = models.DateField('opening date')
    no_of_shares = models.DecimalField(max_digits=19, decimal_places=0)


class Income(models.Model):
    income_name = models.CharField(max_length=10)
    income_description = models.CharField(max_length=50)
    income_currency = models.CharField(max_length=10)
    income_current_balance = models.DecimalField(max_digits=19,
                                                 decimal_places=2)


class Expense(models.Model):
    expense_name = models.CharField(max_length=10)
    expense_description = models.CharField(max_length=50)
    expense_currency = models.CharField(max_length=10)
    expense_current_balance = models.DecimalField(max_digits=19,
                                                  decimal_places=2)


class Account(models.Model):
    account_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10)
    account_name = models.CharField(max_length=50)
    account_code = models.CharField(max_length=50)
    account_currency_security = models.CharField(max_length=10)
    account_initial_balance = models.DecimalField(max_digits=19,
                                                  decimal_places=2)
    account_current_balance = models.DecimalField(max_digits=19,
                                                  decimal_places=2)
    account_open_date = models.DateField('opening date')


class Transactions(models.Model):
    transfer_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transfer_date = models.DateTimeField('transaction date')
    transfer_description = models.CharField(max_length=50)
    transfer_target = models.CharField(max_length=20)
    transfer_cleared = models.BooleanField()
    transfer_deposit = models.DecimalField(max_digits=19, decimal_places=2)
    transfer_withdrawal = models.DecimalField(max_digits=19, decimal_places=2)
    transfer_balance = models.DecimalField(max_digits=19, decimal_places=2)
    transfer_conversion_rate = models.DecimalField(max_digits=19,
                                                   decimal_places=6)
    transfer_fee = models.DecimalField(max_digits=19, decimal_places=2)
