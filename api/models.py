from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    USER_STATUS_TYPE = (
        ('S', 'Student'),
        ('T', 'Teacher')
    )

    user_status = models.CharField(max_length=1,
                                   choices=USER_STATUS_TYPE,
                                   default='S')

    REQUIRED_FIELDS = ['password', 'email', 'user_status']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Course(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Teachers = models.ManyToManyField(User, related_name='Teachers',
                                      blank=True)
    Students = models.ManyToManyField(User, related_name='Students',
                                      blank=True)

    def __str__(self):
        return self.Name


class Lecture(models.Model):
    Theme = models.CharField(max_length=70)
    Presentation = models.FileField(upload_to='static/presentation')
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.Theme


class Homework(models.Model):
    Homework_theme = models.CharField(max_length=70)
    Homework_text = models.TextField()
    Lecture = models.ForeignKey(Lecture, related_name='Homework',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.Homework_theme


class HomeworkSolution(models.Model):
    Solution = models.FileField(upload_to='static/solution')
    Task = models.ForeignKey(Homework, related_name='Solution',
                             on_delete=models.CASCADE)
    Student = models.ForeignKey(User, related_name='Student',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.Task


class TaskMark(models.Model):
    Mark = models.PositiveSmallIntegerField()
    Solution = models.ForeignKey(HomeworkSolution, related_name='Mark',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.Mark


class MarkComment(models.Model):
    Comment = models.TextField()
    Comment_author = models.ForeignKey(User,
                                       related_name='Comment_author',
                                       on_delete=models.CASCADE)
    mark = models.ForeignKey(TaskMark, related_name='CommentMark',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment
