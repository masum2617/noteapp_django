# Generated by Django 3.2 on 2021-05-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name_plural': 'Notes'},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='creator',
        ),
    ]
