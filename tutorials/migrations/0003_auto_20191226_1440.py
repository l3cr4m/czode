# Generated by Django 2.2.7 on 2019-12-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_part_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='order',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
