# Generated by Django 3.0.6 on 2020-06-22 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitglieder', '0004_auto_20200616_1500'),
        ('checklisten', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkliste',
            name='mitglied',
        ),
        migrations.AddField(
            model_name='checkliste',
            name='mitgliedAmt',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mitglieder.MitgliedAmt'),
            preserve_default=False,
        ),
    ]