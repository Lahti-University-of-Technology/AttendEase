# Generated by Django 4.2.6 on 2023-11-13 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('attendease', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendace', to='users.student'),
        ),
    ]