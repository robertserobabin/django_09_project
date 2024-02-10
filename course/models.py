from datetime import date

from django.db import models

from config import settings
from lesson.models import Lesson
from user.models import User


class Course(models.Model):

    name = models.CharField(max_length=50, verbose_name="name")
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()
    lessons = models.ManyToManyField(Lesson, related_name='courses')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Paying(models.Model):

    METHOD_CHOICES = [
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_to_pay = models.DateField(default=date.today)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='paying', null=True, blank=True)
    sum = models.PositiveIntegerField()
    method_to_pay = models.CharField(max_length=10, choices=METHOD_CHOICES)

class CourseSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscribers')
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.full_name} - {self.course.name}'