# Generated by Django 4.2 on 2023-04-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educapedia', '0012_alter_courses_assignment_alter_courses_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='instructor',
            field=models.CharField(default='Test', max_length=100),
        ),
    ]
