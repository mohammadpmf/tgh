# Generated by Django 4.0.3 on 2022-08-02 13:36

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('food', models.CharField(max_length=100)),
            ],
        ),
    ]
