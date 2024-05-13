from django.contrib.auth.models import User
from django.db import models


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# Модель пользовательских данных
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.name
