from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200,default=None)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.question



