# Generated by Django 5.0.3 on 2024-06-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinSaver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_one', models.FileField(blank=True, default=None, null=True, upload_to='audit_file/', verbose_name='Audit File One')),
                ('file_two', models.FileField(blank=True, default=None, null=True, upload_to='audit_file/', verbose_name='Audit File two')),
            ],
        ),
    ]
