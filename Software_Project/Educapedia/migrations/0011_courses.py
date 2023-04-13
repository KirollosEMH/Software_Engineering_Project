# Generated by Django 4.2 on 2023-04-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educapedia', '0010_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('math', 'Math'), ('science', 'Science'), ('ict', 'ICT')], max_length=10)),
                ('video1', models.FileField(upload_to='videos/')),
                ('video2', models.FileField(upload_to='videos/')),
                ('quiz', models.FileField(upload_to='quizzes/')),
                ('assignment', models.FileField(upload_to='assignments/')),
                ('picture', models.ImageField(upload_to='pictures/')),
            ],
        ),
    ]
