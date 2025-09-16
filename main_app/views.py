from django.shortcuts import render
from django.http import HttpResponse
from .models import Application

def about(request):
    return render(request, 'about.html')

def app_index(request):
    applications = Application.objects.all().order_by('-applied_date')
    return render(request, 'applications/index.html', {'applications': applications})

def home(request):
    return render(request, 'home.html')

class Application:
    def __init__(self, company, position, status, description, applied_date):
        self.company = company
        self.position = position
        self.status = status          
        self.description = description
        self.applied_date = applied_date  

applications = [
    Application('Acme Corp', 'Backend Developer', 'Applied', 'Python/Django focus', '2025-09-10'),
    Application('Globex', 'Full-Stack Engineer', 'Interview', 'React + Django, 2 rounds done', '2025-08-29'),
    Application('Initech', 'DevOps Engineer', 'Rejected', 'Strong infra, waiting period ended', '2025-08-20'),
    Application('Umbrella', 'Data Engineer', 'Offer', 'ETL + warehouses, offer pending review', '2025-09-12'),
]






