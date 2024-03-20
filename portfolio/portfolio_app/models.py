from django.db import models
from django.contrib.auth.models import User


genre = (
    ('engineering','engineering'),
    ('personal', 'personal'),
)
COUNTRY_CODES = (
    ('+91', '+91 - India'),
    # Add more country codes as needed
)

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.institution

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    date_earned = models.DateField()

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=genre, default='misc')
    image = models.ImageField(upload_to ='uploads/', default = "uploads/default-image.jpg")
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    phone_country_code = models.CharField(max_length=5, choices=COUNTRY_CODES, default="+91")
    phone_number = models.CharField(max_length=15)  # Adjust the max_length as per your requirements
    email = models.EmailField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name
    

class Meta:
    app_label = 'portfolio_app'