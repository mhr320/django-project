# Generated by Django 2.2.2 on 2019-06-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190612_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='forcedmovepost',
            name='ops_inits',
            field=models.CharField(default='==', max_length=4),
        ),
    ]
