from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Recruiter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company} ({self.job_title})"

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    candidates = models.ManyToManyField(Candidate, related_name='job_offers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.recruiter.company}"
