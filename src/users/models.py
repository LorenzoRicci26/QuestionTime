from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This allows for additional fields and methods in the future if needed.
    """
    # Add any additional fields here if necessary
    pass


