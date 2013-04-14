from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registration.models import RegistrationProfile


# Make sure we create a MyCustomProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        RegistrationProfile.objects.create(user=instance)

post_save.connect(create_facebook_profile, sender=User)
