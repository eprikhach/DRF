# Generated by Django 3.2.3 on 2022-05-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210607_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_status',
            field=models.CharField(choices=[('ST', 'Student'), ('TE', 'Teacher')], default='S', max_length=2),
        ),
    ]
