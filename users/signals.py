# HERE WE CREATE A PROFILE AUTOMATICALLY WHEN A USER IS CREATED

# this gets fired when an user is created
from django.db.models.signals import post_save

# the user model will be a sender
from django.contrib.auth.models import User

# we also need to import receiver
from django.dispatch import receiver

# we want to import Profile from our models as we will be creating a new profile
from .models import Profile

# This means fire the post_save when the User(sender) is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if there is something created in the User model then do this
    if created:
        Profile.objects.create(user=instance) #this creates the profile

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() #this saves the profile to the db