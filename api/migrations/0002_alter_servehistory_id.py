# Generated by Django 3.2.11 on 2022-03-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servehistory',
            name='id',
            field=models.CharField(default='7KJW', editable=False, max_length=4, primary_key=True, serialize=False, unique=True),
        ),
    ]
