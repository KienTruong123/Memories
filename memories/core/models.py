from django.conf import settings
from django.db import models
from django.forms import DecimalField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class MemoryPlace(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    comment = models.TextField(max_length=500, blank=False, null=False)
    long = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    created_at = models.DateTimeField(default=timezone.datetime.now())
