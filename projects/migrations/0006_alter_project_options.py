# Generated by Django 4.0.1 on 2022-01-18 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20211118_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', 'vote_total', 'title']},
        ),
    ]
