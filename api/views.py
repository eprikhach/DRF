from django.db.models import Q
from loguru import logger
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import api.serializers as api_serializers
import api.permissions as api_permissions
import api.models as api_models
from rest_framework.request import Request
import requests



class UserActivationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


class TeacherCourseList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = api_serializers.CourseSerializer

    def get_queryset(self):
        return api_models.Course.objects.filter(
            Teachers__pk=self.request.user.id)


class StudentCourseList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = api_serializers.CourseSerializer

    def get_queryset(self):
        return api_models.Course.objects.filter(Students__pk=
                                                self.request.user.id)


class CourseCreate(generics.CreateAPIView):
    permission_classes = [api_permissions.IsTeacher, ]
    serializer_class = api_serializers.CourseSerializer

    queryset = api_models.Course.objects.all()


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.CourseRUDSerializer

    queryset = api_models.Course.objects.all()


class LectureList(generics.ListAPIView):
    permission_classes = [api_permissions.IsTeacherMemberOrReadOnly, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class LectureCreate(generics.CreateAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class HomeworkList(generics.ListAPIView):
    permission_classes = [api_permissions.IsTeacherMemberOrReadOnly, ]
    serializer_class = api_serializers.HomeworkSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkCreate(generics.CreateAPIView):
    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkRUDSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkSolutionList(generics.ListAPIView):
    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class HomeworkStudentSolutionList(generics.ListAPIView):
    permission_classes = [api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    def get_queryset(self):
        return api_models.HomeworkSolution.objects.filter(
            Student__pk=self.request.user.id)


class HomeworkSolutionCreate(generics.CreateAPIView):
    permission_classes = [api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class HomeworkSolutionRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [api_permissions.IsStudentSolution,
                          api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class MarkList(generics.ListAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkSerializer

    queryset = api_models.TaskMark.objects.all()


class StudentMarkList(generics.ListAPIView):
    permission_classes = [api_permissions.IsStudentMember, ]
    serializer_class = api_serializers.MarkSerializer
    lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return api_models.TaskMark.objects.filter(
            Solution=self.kwargs['homework_id'])


class CreateMark(generics.CreateAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkSerializer

    queryset = api_models.TaskMark.objects.all()


class MarkRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkRUDSerializer

    queryset = api_models.TaskMark.objects.all()


class CommentCreate(generics.CreateAPIView):
    permission_classes = [api_permissions.IsSelfSolutionOrTeacherMember, ]
    serializer_class = api_serializers.CommentSerializer

    queryset = api_models.MarkComment.objects.all()


class CommentList(generics.ListAPIView):
    permission_classes = [api_permissions.IsSelfSolutionOrTeacherMember, ]
    serializer_class = api_serializers.CommentSerializer

    queryset = api_models.MarkComment.objects.all()
