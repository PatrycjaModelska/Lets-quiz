from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True, null=True)

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/default_profile.png"

    def __str__(self):
        return self.user.username
