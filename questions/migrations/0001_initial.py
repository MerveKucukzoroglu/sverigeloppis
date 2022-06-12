# Generated by Django 3.2 on 2022-06-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loppises', '0003_alter_loppis_county'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('loppis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='loppises.loppis')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
