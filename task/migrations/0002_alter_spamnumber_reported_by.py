# Generated by Django 4.2.7 on 2023-11-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spamnumber',
            name='reported_by',
            field=models.ManyToManyField(related_name='reported_by', to='task.contact'),
        ),
    ]
