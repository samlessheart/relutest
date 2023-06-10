from django.db import models
from django.contrib.auth.models import AbstractUser


# customusermodel 

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    # school = models.models.ForeignKey("CustomUser", null= True , blank= True , on_delete=models.CASCADE)
