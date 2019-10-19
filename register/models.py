from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")