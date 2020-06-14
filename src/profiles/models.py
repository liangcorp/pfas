from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    app_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        null=True)

    birthday = models.DateField()
