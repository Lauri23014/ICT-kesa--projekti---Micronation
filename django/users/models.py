from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

#one to one relationship between the user and profile.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  #on_dele deletes user profile automatically when the user is deleted
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")
    theme_color = models.CharField(max_length=7, default='#1a1a1a')
    favorite_cat = models.CharField(max_length=100, blank=True, null=True)
    background_image = models.ImageField(upload_to='profile_backgrounds/', blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        if self.background_image:
            img_path = self.background_image.path
            img = Image.open(img_path)
            max_size = (1920, 1080)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            img.save(img_path)
            

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

