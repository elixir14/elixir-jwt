from django.contrib.auth.models import User
from django.db import models


class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='token_user')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("token", "user")
        verbose_name = "Black Listed Token"
        verbose_name_plural = "Black Listed Tokens"
        ordering = ['-timestamp']
