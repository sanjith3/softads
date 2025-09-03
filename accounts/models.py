# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    mobile_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[0-9]{10}$",
                message="Enter a valid 10-digit mobile number.",
            )
        ],
        help_text="User's mobile number used for login.",
        blank=False,
        null=True,
    )
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile_number or self.username