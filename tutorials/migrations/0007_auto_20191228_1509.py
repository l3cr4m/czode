# Generated by Django 3.0 on 2019-12-28 14:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20191227_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]