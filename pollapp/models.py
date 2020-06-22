from django.db import models

# Create your models here.
class Question(models.Model):
    question_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_name

class Choice(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    choices = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choices