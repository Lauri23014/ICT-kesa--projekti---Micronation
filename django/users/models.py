from django.db import models

from django.contrib.auth.models import User

#one to one relationship between the user and profile.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  #on_dele deletes user profile automatically when the user is deleted
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")


    def __str__(self):
        return str(self.user)
