# Generated by Django 5.1.3 on 2024-12-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=32)),
                ('quantity', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]