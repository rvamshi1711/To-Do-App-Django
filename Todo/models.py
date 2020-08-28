from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class T(models.Model):
    content=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)