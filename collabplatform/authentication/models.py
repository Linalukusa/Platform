from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png', blank=True)



class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    ETHNICITY_CHOICES = [
        ('AA', 'African American'),
        ('AI', 'American Indian or Native Alaskan'),
        ('API', 'Asian or Pacific Islander'),
        ('HL', 'Hispanic-Latino'),
        ('W', 'White'),
        ('O', 'Other'),
    ]
    ethnicity = models.CharField(max_length=3, choices=ETHNICITY_CHOICES)
    religion = models.CharField(max_length=100)
    open_to_religious_school = models.BooleanField(default=False)
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    ANNUAL_INCOME_CHOICES = [
        ('0-10k', '0 - 10,000'),
        ('10k-30k', '10,001 - 30,000'),
        ('30k-50k', '30,001 - 50,000'),
        ('50k-75k', '50,001 - 75,000'),
        ('75k-100k', '75,001 - 100,000'),
        ('100k+', '100,000+'),
    ]
    annual_family_income = models.CharField(max_length=20, choices=ANNUAL_INCOME_CHOICES)
    first_generation_college_student = models.BooleanField(default=False)

    EDUCATION_LEVEL_CHOICES = [
        ('', 'Choose Education Level'),  # Default option
        ('High School', 'High School'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('PhD', 'PhD'),
        ('Other', 'Other'),
    ]
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES, default='')

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
        return f"{self.first_name} {self.last_name}"
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

