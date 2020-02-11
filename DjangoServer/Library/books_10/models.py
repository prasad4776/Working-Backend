
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    price = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.name