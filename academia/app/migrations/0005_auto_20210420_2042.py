# Generated by Django 3.0.5 on 2021-04-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_curso_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='texto',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]