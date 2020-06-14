from django.db import models
from appuser.models import AppUser


# Create your models here.
class Profile(models.Model):
    app_user = models.ForeignKey(AppUser,
                                 on_delete=models.CASCADE,
                                 related_name="profile",
                                 null=True)
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    birthday = models.DateField()
