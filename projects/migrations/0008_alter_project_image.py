# Generated by Django 3.2.3 on 2021-06-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='media/'),
        ),
    ]
