# Generated by Django 2.0.3 on 2018-03-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180321_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='roles', to='core.Role'),
        ),
    ]
