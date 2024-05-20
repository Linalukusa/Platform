# Generated by Django 5.0.6 on 2024-05-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='major',
            field=models.CharField(choices=[('', 'Choose a Major'), ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Business Administration', 'Business Administration'), ('Psychology', 'Psychology'), ('Biology', 'Biology'), ('Mathematics', 'Mathematics'), ('English Literature', 'English Literature'), ('History', 'History'), ('Art', 'Art'), ('Music', 'Music'), ('Other', 'Other')], default='', max_length=100),
        ),
    ]