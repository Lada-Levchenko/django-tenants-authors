from django.db import models

from customers.models import Client


class Article(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
