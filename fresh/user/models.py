from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()

class User(models.Model):
    name = models.ForeignKey(
        to=USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
    )
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)
    store_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.email