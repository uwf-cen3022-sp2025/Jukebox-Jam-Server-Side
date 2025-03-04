from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)

    check_email_confirm = models.BooleanField(default=False)
    
    def __str__(self):
         return self.username