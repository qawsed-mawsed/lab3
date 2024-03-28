from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля профиля пользователя
    # Например:
    # date_of_birth = models.DateField(blank=True, null=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username
