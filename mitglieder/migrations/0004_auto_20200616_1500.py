# Generated by Django 3.0.7 on 2020-06-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitglieder', '0003_auto_20200616_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prevmitgliedamt',
            name='members',
            field=models.ManyToManyField(to='mitglieder.Mitglied'),
        ),
    ]