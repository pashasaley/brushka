from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import models as models
from django.contrib.auth import models as mod


def get_id(name):
    _k = Users.objects.values('id').filter(key=name)
    id_user = _k.all()[0]['id']
    return id_user


class Users(mod.User):
    key = models.CharField(max_length=32)


@receiver(pre_save, sender=Users)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")
