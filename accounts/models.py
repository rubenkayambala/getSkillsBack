from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class CustomUser(AbstractUser):
    post_name = models.CharField(('post_name'), max_length=50)
    birthday = models.CharField(('birthday'), max_length=15)
    adress = models.CharField(('adress'), max_length=100)
    phone = models.CharField(('phone'), max_length=15)
    picture = models.ImageField(('picture'), upload_to='picture')

    objects = UserManager()

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'