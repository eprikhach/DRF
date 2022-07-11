from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Stores a user entries.
    """
    student = "ST"
    teacher = "TE"

    user_status_type = [(student, "Student"), (teacher, "Teacher")]

    user_status = models.CharField(max_length=2,
                                   choices=user_status_type,
                                   default='ST')

    REQUIRED_FIELDS = ['password', 'email', 'user_status']

    def __str__(self):
        return self.username


class Course(models.Model):
    """
    Stores a course entries, related to :model: 'teachers.User' and
    :model: 'students.User'.
    """

    name = models.CharField(max_length=50)
    description = models.TextField()
    teachers = models.ManyToManyField(User, related_name='Teachers',
                                      blank=True)
    students = models.ManyToManyField(User, related_name='Students',
                                      blank=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    """
    Stores a lecture entries, related to :model: 'course.Course'.
    """

    theme = models.CharField(max_length=70)
    presentation = models.FileField(upload_to='static/presentation')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.theme


class Homework(models.Model):
    """
    Stores a homework entries, related to :model: 'lecture.Lecture'.
    """

    homework_theme = models.CharField(max_length=70)
    homework_text = models.TextField()
    lecture = models.ForeignKey(Lecture, related_name='Homework',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.homework_theme


class HomeworkSolution(models.Model):
    """
    Stores a homework solution entries, related to :model: 'task.Homework'
    and :model: 'student.User'.
    """

    solution = models.FileField(upload_to='static/solution')
    task = models.ForeignKey(Homework, related_name='Solution',
                             on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='Student',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.task


class TaskMark(models.Model):
    """
    Stores a task mark entries, related to :model: 'solution.HomeworkSolution'.
    """

    mark = models.PositiveSmallIntegerField()
    solution = models.ForeignKey(HomeworkSolution, related_name='Mark',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.mark


class MarkComment(models.Model):
    """
    Stores mark comment entries, related to :model: 'comment_author.User'
    and :model: 'mark.TaskMark'.
    """

    comment = models.TextField()
    comment_author = models.ForeignKey(User,
                                       related_name='Comment_author',
                                       on_delete=models.CASCADE)
    mark = models.ForeignKey(TaskMark, related_name='CommentMark',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
