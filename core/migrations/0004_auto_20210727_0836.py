# Generated by Django 3.2.5 on 2021-07-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210727_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_of_death',
            field=models.DateField(null=True),
        ),
    ]
