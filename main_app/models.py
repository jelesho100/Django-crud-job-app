from django.db import models

class Application(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Applied', 'Applied'),
            ('Interview', 'Interview'),
            ('Offer', 'Offer'),
            ('Rejected', 'Rejected'),
        ],
        default='Applied',
    )
    applied_date = models.DateField()

    def __str__(self):
        return f"{self.company} — {self.position}"

