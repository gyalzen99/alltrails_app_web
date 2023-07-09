from django.db import models
from django.contrib.auth.models import User, AnonymousUser

class UserProfileModel(models):
    user = models.ForeignKey(User, default=AnonymousUser)
    user_image = models.ImageField(upload_to='images/profile', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

