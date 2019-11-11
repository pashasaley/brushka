from django.db import models
from editor.models import TShirts
from django.contrib.auth.models import User


class Comments(models.Model):
    id_ts = models.ForeignKey(TShirts, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
