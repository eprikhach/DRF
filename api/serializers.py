from rest_framework import serializers
import api.models as api_models


class CourseSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the course table."""

    class Meta:
        model = api_models.Course
        fields = ('id', 'name', 'description', 'teachers', 'students')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Custom create method, which auto adding user to course owner field.

        :param validated_data: request data
        :return: json
        """

        name = validated_data['name']
        description = validated_data['description']
        data = api_models.Course.objects.create(name=name,
                                                description=description)
        data.save()

        data.teachers.add(self.context['request'].user.pk)

        return data


class CourseRUDSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with rud
    operations on the Course table."""

    class Meta:
        model = api_models.Course
        fields = ('id', 'name', 'description', 'teachers', 'students')
        read_only_fields = ('id',)


class LectureSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the homework table."""

    class Meta:
        model = api_models.Lecture
        fields = ('id', 'theme', 'presentation', 'course')
        read_only_fields = ('id', 'course')

    def create(self, validated_data):
        """Custom create method, which auto attach course id to lecture.

        :param validated_data: request data
        :return: data
        """

        course_id = self.context['view'].kwargs['course_id']
        course = api_models.Course.objects.get(id=course_id)
        theme = validated_data['theme']
        presentation = validated_data['presentation']
        data = api_models.Lecture.objects.create(
            course=course,
            theme=theme,
            presentation=presentation)

        data.save()

        return data


class LectureRUDSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with rud
    operations on the Lecture table."""

    class Meta:
        model = api_models.Lecture
        fields = ('id', 'theme', 'presentation', 'course')
        read_only_fields = ('id', 'course')


class HomeworkSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the homework table."""
    class Meta:
        model = api_models.Homework
        fields = ('id', 'homework_theme', 'homework_text', 'lecture')
        read_only_fields = ('id', 'lecture')

    def create(self, validated_data):
        """Custom create method, which auto attach lecture id to homework.

        :param validated_data: request data
        :return: data
        """
        lecture_id = self.context['view'].kwargs['lecture_id']
        lecture = api_models.Lecture.objects.get(id=lecture_id)
        homework_theme = validated_data['homework_theme']
        homework_text = validated_data['homework_text']
        data = api_models.Homework.objects.create(
            lecture=lecture,
            homework_theme=homework_theme,
            homework_text=homework_text)

        data.save()

        return data


class HomeworkRUDSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with rud
    operations on the homework table."""

    class Meta:
        model = api_models.Homework
        fields = ('id', 'homework_theme', 'homework_text', 'lecture')
        read_only_fields = ('id', 'lecture')


class HomeworkSolutionSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the homework_solution table."""

    class Meta:
        model = api_models.HomeworkSolution
        fields = ('id', 'task', 'solution', 'student')
        read_only_fields = ('id', 'task', 'student')

    def create(self, validated_data):
        """Custom create method, which auto attach current user and homework
        id to homework solution.

        :param validated_data: request data
        :return: data
        """
        task_id = self.context['view'].kwargs['homework_id']
        task = api_models.Homework.objects.get(id=task_id)
        user = self.context['request'].user
        solution = validated_data['solution']

        data = api_models.HomeworkSolution.objects. \
            create(student=user,
                   task=task,
                   solution=solution)

        data.save()
        return data


class HomeworkSolutionRUD(serializers.ModelSerializer):
    """Class, which serializes the request object for working with rud
    operations on the homework_solution table."""

    class Meta:
        model = api_models.HomeworkSolution
        fields = ('id', 'task', 'solution', 'student')
        read_only_fields = ('id', 'task')


class MarkSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the mark table."""

    class Meta:
        model = api_models.TaskMark
        fields = ('id', 'mark', 'solution')
        read_only_fields = ('id', 'solution')

    def create(self, validated_data):
        """Custom create method, which auto attach solution id to mark."""
        solution_id = self.context['view'].kwargs['solution_id']
        solution = api_models.HomeworkSolution.objects.get(
            id=solution_id)

        mark = validated_data['Mark']

        data = api_models.TaskMark.objects.create(solution=solution,
                                                  mark=mark)

        data.save()

        return data


class MarkRUDSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with rud
    operations on the mark table."""
    class Meta:
        model = api_models.TaskMark
        fields = ('id', 'mark', 'solution')
        read_only_fields = ('id', 'solution')


class CommentSerializer(serializers.ModelSerializer):
    """Class, which serializes the request object for working with create
    operation on the comment table."""
    class Meta:
        model = api_models.MarkComment
        fields = ('id', 'comment', 'comment_author', 'mark')
        read_only_fields = ('id', 'comment_author', 'mark')

    def create(self, validated_data):
        """Custom create method, which auto attach current user and mark id
        to comment."""
        mark_id = self.context['view'].kwargs['mark_id']
        mark = api_models.TaskMark.objects.get(id=mark_id)
        user = self.context['request'].user
        comment = validated_data['comment']

        data = api_models.MarkComment.objects.create(
            comment_author=user,
            mark=mark,
            comment=comment
        )

        data.save()

        return data
