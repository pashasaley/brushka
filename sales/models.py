from django.db import models
from editor.models import TShirts
from django.contrib.auth.models import User
from datetime import datetime


class Comments(models.Model):
    id_ts = models.ForeignKey(TShirts, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()


class BuyTShirts(models.Model):
    id_ts = models.ForeignKey(TShirts, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.CharField(max_length=254)
    name = models.CharField(max_length=30)
