# Generated by Django 4.1 on 2022-08-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dob', '0003_alter_wishes_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
