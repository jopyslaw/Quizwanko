from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    answer_a = models.CharField(max_length=150)
    answer_b = models.CharField(max_length=150)
    answer_c = models.CharField(max_length=150)
    answer_d = models.CharField(max_length=150)
    good_answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question


class LeaderBoard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    points = models.IntegerField()

    def __str__(self):
        return self.username
