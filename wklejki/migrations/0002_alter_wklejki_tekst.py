# Generated by Django 4.1.3 on 2022-12-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wklejki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wklejki',
            name='tekst',
            field=models.TextField(blank=True, max_length=2137, null=True),
        ),
    ]