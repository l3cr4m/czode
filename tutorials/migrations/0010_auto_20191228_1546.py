# Generated by Django 3.0 on 2019-12-28 14:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_auto_20191228_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
