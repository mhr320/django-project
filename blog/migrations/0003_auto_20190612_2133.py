# Generated by Django 2.2.2 on 2019-06-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_forcedmovepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forcedmovepost',
            name='forced_shift',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='forcedmovepost',
            name='original_shift',
            field=models.CharField(max_length=4),
        ),
    ]
