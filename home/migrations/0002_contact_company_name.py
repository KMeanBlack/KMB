# Generated by Django 4.1.5 on 2024-11-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
