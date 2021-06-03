from loguru import logger
from rest_framework import serializers
import api.models as api_models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Course
        fields = ('id', 'Name', 'Description', 'Teachers', 'Students')
        read_only_fields = ('id',)

    def create(self, validated_data):
        name = validated_data['Name']
        description = validated_data['Description']
        data = api_models.Course.objects.create(Name=name,
                                                Description=description)
        data.save()

        data.Teachers.add(self.context['request'].user.pk)

        return data


class CourseRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Course
        fields = ('id', 'Name', 'Description', 'Teachers', 'Students')
        read_only_fields = ('id',)


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Lecture
        fields = ('id', 'Theme', 'Presentation', 'Course')
        read_only_fields = ('id', 'Course')

    def create(self, validated_data):
        course_id = self.context['view'].kwargs['course_id']
        course = api_models.Course.objects.get(id=course_id)
        theme = validated_data['Theme']
        presentation = validated_data['Presentation']
        data = api_models.Lecture.objects.create(
            Course=course,
            Theme=theme,
            Presentation=presentation)

        data.save()

        return data


class LectureRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Lecture
        fields = ('id', 'Theme', 'Presentation', 'Course')
        read_only_fields = ('id', 'Course')


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Homework
        fields = ('id', 'Homework_theme', 'Homework_text', 'Lecture')
        read_only_fields = ('id', 'Lecture')

    def create(self, validated_data):
        lecture_id = self.context['view'].kwargs['lecture_id']
        logger.info(lecture_id)
        lecture = api_models.Lecture.objects.get(id=lecture_id)
        homework_theme = validated_data['Homework_theme']
        homework_text = validated_data['Homework_text']
        data = api_models.Homework.objects.create(
            Lecture=lecture,
            Homework_theme=homework_theme,
            Homework_text=homework_text)

        data.save()

        return data


class HomeworkRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Homework
        fields = ('id', 'Homework_theme', 'Homework_text', 'Lecture')
        read_only_fields = ('id', 'Lecture')


class HomeworkSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.HomeworkSolution
        fields = ('id', 'Task', 'Solution', 'Student')
        read_only_fields = ('id', 'Task', 'Student')

    def create(self, validated_data):
        task_id = self.context['view'].kwargs['homework_id']
        task = api_models.Homework.objects.get(id=task_id)
        user = self.context['request'].user
        solution = validated_data['Solution']

        data = api_models.HomeworkSolution.objects. \
            create(Student=user,
                   Task=task,
                   Solution=solution)

        data.save()
        return data


class HomeworkSolutionRUD(serializers.ModelSerializer):
    class Meta:
        model = api_models.HomeworkSolution
        fields = ('id', 'Task', 'Solution', 'Student')
        read_only_fields = ('id', 'Task')


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.TaskMark
        fields = ('id', 'Mark', 'Solution')
        read_only_fields = ('id', 'Solution')

    def create(self, validated_data):
        solution_id = self.context['view'].kwargs['solution_id']
        solution = api_models.HomeworkSolution.objects.get(
            id=solution_id)

        mark = validated_data['Mark']

        data = api_models.TaskMark.objects.create(Solution=solution,
                                                  Mark=mark)

        data.save()

        return data


class MarkRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.TaskMark
        fields = ('id', 'Mark', 'Solution')
        read_only_fields = ('id', 'Solution')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.MarkComment
        fields = ('id', 'Comment', 'Comment_author', 'mark')
        read_only_fields = ('id', 'Comment_author', 'mark')

    def create(self, validated_data):
        mark_id = self.context['view'].kwargs['mark_id']
        mark = api_models.TaskMark.objects.get(id=mark_id)
        user = self.context['request'].user
        comment = validated_data['Comment']

        data = api_models.MarkComment.objects.create(
            Comment_author=user,
            mark=mark,
            Comment=comment
        )

        data.save()

        return data
