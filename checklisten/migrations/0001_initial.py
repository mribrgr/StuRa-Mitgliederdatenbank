# Generated by Django 3.0.7 on 2020-06-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mitglieder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aufgabe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Checkliste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mitglied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mitglieder.Mitglied')),
            ],
        ),
        migrations.CreateModel(
            name='ChecklisteAufgabe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abgehakt', models.BooleanField(default=False)),
                ('aufgabe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklisten.Aufgabe')),
                ('checkliste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklisten.Checkliste')),
            ],
        ),
    ]
