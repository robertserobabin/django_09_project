from django.db import models



class Lesson(models.Model):
    name = models.CharField(max_length=50)
    preview = models.ImageField(null=True, blank=True)
    description = models.TextField()
    link = models.TextField()
