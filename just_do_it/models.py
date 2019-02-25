from django.db import models

# Create your models here.

RUBRIC_CHOICES = (
    ('READ', 'Прочитать'),
    ('BUY', 'Купить'),
    ('TO_DO', 'Сделать'),
    ('OTHER', 'Другое')
    )   

class Rubric(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Target(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    complete = models.BooleanField()

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=300)
    start_date = models.DateField()
    finish_date = models.DateField()
    complete = models.BooleanField()
    #rubric = models.CharField(max_length=10, choices=RUBRIC_CHOICES, default='OTHER')
    target = models.ForeignKey(Target, on_delete=models.CASCADE, blank=True, null=True)
    rubric = models.ForeignKey(Rubric, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']
