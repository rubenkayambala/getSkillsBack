from django.db import models
from accounts.models import CustomUser

PROMOTION = (
    ('promotion1', 'Promotion 1'),
    ('promotion2', 'Promotion 2'),
    ('promotion3', 'Promotion 3'),
    ('promotion4', 'Promotion 4'),
)

class Formation(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='formation/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Album(models.Model):
    promotion = models.CharField(choices=PROMOTION, max_length=50)
    file = models.FileField(upload_to='album/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.promotion} - {self.file}'

class Carte(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    matricule = models.CharField(max_length=10)
    full_name = models.CharField(max_length=80)
    picture = models.FileField(upload_to='picture/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.matricule}'

class Certificat(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    matricule = models.CharField(max_length=10)
    full_name = models.CharField(max_length=80)
    picture = models.FileField(upload_to='picture/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.matricule}'