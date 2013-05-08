from django_facebook.models import FacebookProfileModel
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registration.models import RegistrationProfile


class MyCustomProfile(FacebookProfileModel):
    user = models.OneToOneField(User)
    

# Make sure we create a MyCustomProfile when creating a User
def create_facebook_profile(sender, instance, created, **kwargs):
    if created:
        RegistrationProfile.objects.create(user=instance)

def save(self, *args, **kwargs):
    try:
        existing = UserExtension.objects.get(user=self.user)
        self.id = existing.id #force update instead of insert
    except UserExtension.DoesNotExist:
        pass 
    models.Model.save(self, *args, **kwargs)

post_save.connect(create_facebook_profile, sender=User)

