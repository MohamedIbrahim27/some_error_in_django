# Generated by Django 5.0.6 on 2024-06-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_modelname_options_alter_modelname_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelname',
            name='namess',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
