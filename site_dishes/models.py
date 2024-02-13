from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    steps = models.TextField(max_length=10000)
    ingredients = models.TextField(max_length=500)
    time = models.TimeField(default='1:00')
    portions = models.IntegerField(default=1)
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
