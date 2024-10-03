from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class User(get_user_model()):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)


class Employer(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null="", blank=True)


class Vacancy(models.Model):
    def __str__(self):
        return f"{self.author}'s vacancy {self.id}"
    author = models.ForeignKey(Employer, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    salary_per_month = models.IntegerField(default=0)

