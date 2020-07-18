# Generated by Django 3.0.6 on 2020-06-29 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aemter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funktion',
            options={'verbose_name': 'Funktion', 'verbose_name_plural': 'Funktionen'},
        ),
        migrations.AlterModelOptions(
            name='funktionrecht',
            options={'verbose_name': 'Zuordnung Funktion-Recht', 'verbose_name_plural': 'Zuordnungen Funktion-Recht'},
        ),
        migrations.AlterModelOptions(
            name='historicalfunktion',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Funktion'},
        ),
        migrations.AlterModelOptions(
            name='historicalfunktionrecht',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Zuordnung Funktion-Recht'},
        ),
        migrations.AlterModelOptions(
            name='historicalorganisationseinheit',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Organisationseinheit'},
        ),
        migrations.AlterModelOptions(
            name='historicalrecht',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Recht'},
        ),
        migrations.AlterModelOptions(
            name='historicalunterbereich',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Unterbereich'},
        ),
        migrations.AlterModelOptions(
            name='organisationseinheit',
            options={'verbose_name': 'Organisationseinheit', 'verbose_name_plural': 'Organisationseinheiten'},
        ),
        migrations.AlterModelOptions(
            name='recht',
            options={'verbose_name': 'Recht', 'verbose_name_plural': 'Rechte'},
        ),
        migrations.AlterModelOptions(
            name='unterbereich',
            options={'verbose_name': 'Unterbereich', 'verbose_name_plural': 'Unterbereiche'},
        ),
    ]