# Generated by Django 3.2 on 2022-05-31 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loppises', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loppis',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Loppises'},
        ),
    ]