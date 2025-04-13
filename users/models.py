from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # فیلدهای اضافه شما (اختیاری)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = 'users_user'  # این خط را اضافه کنید