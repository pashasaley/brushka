from django.db import models
from django.contrib.auth.models import User


class BlockUser(models.Model):
    block = models.BooleanField(default=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
