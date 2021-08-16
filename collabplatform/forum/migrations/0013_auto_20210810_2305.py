# Generated by Django 3.2.4 on 2021-08-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_category_message_subcategory_threadprefix'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Achievement',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='caused_by',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='downvoters',
        ),
        migrations.RemoveField(
            model_name='message',
            name='upvoters',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='ThreadPrefix',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]