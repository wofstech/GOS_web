# Generated by Django 2.0.1 on 2018-03-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0002_auto_20180308_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]
