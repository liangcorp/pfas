from django.db import models


# Create your models here.
class Asset(models.Model):
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

    asset_name = models.CharField(max_length=20)
    asset_description = models.CharField(max_length=30)
    asset_currency = models.CharField(max_length=10)

    asset_initial_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
    asset_current_balance = models.DecimalField(max_digits=19,
                                                decimal_places=2)
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
