from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

INTERACTIONS = (
    ('I', 'Interview'),
    ('A', 'Assessment'),
    ('O', 'Offer'),
    ('R', 'Rejection'),
    ('X', 'Other'),
)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.id})

class Application(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('Applied', 'Applied'), ('Interview', 'Interview'),
                ('Offer', 'Offer'), ('Rejected', 'Rejected')],
        default='Applied',
    )
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    applied_date = models.DateField()

    def __str__(self):
        return f"{self.company} — {self.position}"

    def get_absolute_url(self):
        return reverse('application-detail', kwargs={'pk': self.pk})


class Interaction(models.Model):
    date = models.DateField('Interaction date')
    kind = models.CharField(
        max_length=1,
        choices=INTERACTIONS,
        default=INTERACTIONS[0][0],
    )
    notes = models.TextField(blank=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_kind_display()} on {self.date}"

    class Meta:
        ordering = ['-date']




