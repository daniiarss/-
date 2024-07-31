from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    director = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
