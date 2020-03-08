from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class AuthToken(models.Model):
    user = models.OneToOneField(
        User,
        related_name="user_token",
        on_delete=models.CASCADE,
    )
    token = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )