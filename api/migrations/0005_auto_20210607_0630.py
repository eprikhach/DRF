# Generated by Django 3.2.3 on 2021-06-07 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210602_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Students',
            new_name='students',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Teachers',
            new_name='teachers',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='Homework_text',
            new_name='homework_text',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='Homework_theme',
            new_name='homework_theme',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='Lecture',
            new_name='lecture',
        ),
        migrations.RenameField(
            model_name='homeworksolution',
            old_name='Solution',
            new_name='solution',
        ),
        migrations.RenameField(
            model_name='homeworksolution',
            old_name='Student',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='homeworksolution',
            old_name='Task',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Presentation',
            new_name='presentation',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Theme',
            new_name='theme',
        ),
        migrations.RenameField(
            model_name='markcomment',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='markcomment',
            old_name='Comment_author',
            new_name='comment_author',
        ),
        migrations.RenameField(
            model_name='taskmark',
            old_name='Mark',
            new_name='mark',
        ),
        migrations.RenameField(
            model_name='taskmark',
            old_name='Solution',
            new_name='solution',
        ),
    ]
