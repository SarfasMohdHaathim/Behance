from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import *

def createProfile(sender,instance,created ,**kwargs):
    if created:
        user =instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
post_save.connect(createProfile, sender=User)
