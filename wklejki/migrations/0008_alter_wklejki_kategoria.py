# Generated by Django 4.1.3 on 2022-12-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wklejki', '0007_alter_wklejki_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wklejki',
            name='kategoria',
            field=models.CharField(choices=[('ZWYKLY TEKST', 'ZWYKLY TEKST'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('PHP', 'PHP'), ('PYTHON', 'PYTHON'), ('RUBY', 'RUBY'), ('C', 'C'), ('C++', 'C++'), ('GO', 'GO'), ('LATEX', 'LATEX')], max_length=255),
        ),
    ]
