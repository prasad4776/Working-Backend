from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.first_name







