# Generated by Django 4.0.5 on 2022-06-16 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_portfolio_average_creativity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='average_creativity',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='average_design',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='average_usability',
        ),
    ]
