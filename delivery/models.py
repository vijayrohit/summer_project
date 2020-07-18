from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=200)
    order_list = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
