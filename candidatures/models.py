from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
