from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save, sender=Profile)
# Everytime we add a user it will auto create a Profile for that user


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def updateUser(sender, instance, created, **kwards):
    profile = instance
    user = profile.user
    # if we didn't add created == False, it would trigger createProfile and create
    # an infinite loop
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    # get profile's user (instance is the profile)
    user = instance.user
    # then delete user if deleting profile
    user.delete()
    # we don't need this for the opposite way round as we have cascade


# signals
post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
