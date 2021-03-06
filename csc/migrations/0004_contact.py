# Generated by Django 2.2.6 on 2019-11-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csc', '0003_auto_20191102_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.TextField()),
            ],
        ),
    ]
