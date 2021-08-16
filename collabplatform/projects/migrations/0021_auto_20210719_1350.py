# Generated by Django 3.2.4 on 2021-07-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20210719_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='project',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='project',
            name='leadorganisations',
            field=models.CharField(default='', max_length=500, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectname',
            field=models.CharField(max_length=500, verbose_name='Lead Researcher'),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
    ]
