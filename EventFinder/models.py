from django.db import models
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils.text import slugify
# Create your models here.
from CreateEvent.models import BasicInfo


class Register(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.IntegerField(unique=True)
    email_address = models.EmailField(unique=True)
    event = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)