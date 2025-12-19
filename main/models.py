from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_accent = models.BooleanField(default=False)


class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)
    question = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
