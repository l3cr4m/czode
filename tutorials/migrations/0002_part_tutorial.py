# Generated by Django 2.2.7 on 2019-12-26 13:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('billboard', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('lang', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tutorials.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('order', models.BigIntegerField(default=0, null=True, unique=True)),
                ('billboard', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tutorial', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tutorials.Tutorial')),
            ],
        ),
    ]
