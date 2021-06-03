# Generated by Django 3.2.3 on 2021-05-31 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Students', models.ManyToManyField(related_name='Students', to=settings.AUTH_USER_MODEL)),
                ('Teachers', models.ManyToManyField(related_name='Teachers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Homework_theme', models.CharField(max_length=70)),
                ('Homework_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solution', models.FileField(upload_to='static/solution')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to=settings.AUTH_USER_MODEL)),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Solution', to='api.homework')),
            ],
        ),
        migrations.CreateModel(
            name='TaskMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.PositiveSmallIntegerField()),
                ('Solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mark', to='api.homeworksolution')),
            ],
        ),
        migrations.CreateModel(
            name='MarkComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('Comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_author', to=settings.AUTH_USER_MODEL)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentMark', to='api.taskmark')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theme', models.CharField(max_length=70)),
                ('Presentation', models.FileField(upload_to='static/presentation')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lecture', to='api.course')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='Lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Homework', to='api.lecture'),
        ),
    ]
