from django.db import models


class TShirts(models.Model):
    name_TShirts = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    link_TShirts = models.CharField(max_length=512)
    price = models.IntegerField()
    description = models.TextField()
