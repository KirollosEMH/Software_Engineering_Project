# Generated by Django 4.2 on 2023-04-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educapedia', '0013_courses_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='picture',
            field=models.ImageField(upload_to='static/pictures/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='video1',
            field=models.FileField(upload_to='static/videos/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='video2',
            field=models.FileField(upload_to='static/videos/'),
        ),
    ]
