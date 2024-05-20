from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils import timezone


class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    provider = models.CharField(max_length=200)
    EDUCATION_LEVEL_CHOICES = [
        ('High School', 'High School'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('PhD', 'PhD'),
        ('Other', 'Other'),
    ]
    applicable_education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    MAJOR_CHOICES = [
        ('', 'Choose a Major'),  # Default option
        ('Computer Science', 'Computer Science'),
        ('Engineering', 'Engineering'),
        ('Business Administration', 'Business Administration'),
        ('Psychology', 'Psychology'),
        ('Biology', 'Biology'),
        ('Mathematics', 'Mathematics'),
        ('English Literature', 'English Literature'),
        ('History', 'History'),
        ('Art', 'Art'),
        ('Music', 'Music'),
        ('Other', 'Other'),
    ]
    major = models.CharField(max_length=100, choices=MAJOR_CHOICES, default='')

    def __str__(self):
        return self.title
