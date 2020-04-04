# Generated by Django 3.0.4 on 2020-04-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mitglieder', '0002_auto_20200331_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mitglied',
            name='jabber_id',
        ),
        migrations.RemoveField(
            model_name='mitglied',
            name='mail_privat',
        ),
        migrations.RemoveField(
            model_name='mitglied',
            name='tel_festnetz',
        ),
        migrations.AddField(
            model_name='mitglied',
            name='hausnr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mitglied',
            name='spitzname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mitglied',
            name='ort',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mitglied',
            name='plz',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='mitglied',
            name='strasse',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='MitgliedMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('mitglied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mitglieder.Mitglied')),
            ],
        ),
    ]
