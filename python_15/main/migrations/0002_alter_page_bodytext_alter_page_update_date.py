# Generated by Django 4.2.5 on 2023-09-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='bodytext',
            field=models.TextField(blank=True, verbose_name='Page Content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(verbose_name='Last updated'),
        ),
    ]
