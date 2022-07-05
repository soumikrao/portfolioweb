from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.

class projects(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    content = models.TextField(max_length=5000, default='')
    pub_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class achievements(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    content = models.TextField(max_length=5000, default='')
    pub_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
