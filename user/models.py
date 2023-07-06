from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserModel(AbstractUser):
    usr_img = models.ImageField(upload_to='user/', default='default/icon.png')
