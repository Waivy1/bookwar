# Generated by Django 2.1.3 on 2018-12-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
