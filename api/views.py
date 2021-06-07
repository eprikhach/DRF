from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import api.serializers as api_serializers
import api.permissions as api_permissions
import api.models as api_models
import requests


class UserActivationView(APIView):
    """
    get:
    User activation.

    Activate user using uid and token.
    """

    permission_classes = [AllowAny]

    def get(request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data=post_data)
        return Response(result)


class TeacherCourseList(generics.ListAPIView):
    """
    get:
    Teacher courses list.

    Returns a list of courses with teacher role.
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = api_serializers.CourseSerializer

    def get_queryset(self):
        return api_models.Course.objects.filter(
            Teachers__pk=self.request.user.id)


class StudentCourseList(generics.ListAPIView):
    """
    get:
    Student courses list.

    Returns a list of courses with student role.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = api_serializers.CourseSerializer

    def get_queryset(self):
        return api_models.Course.objects.filter(students__pk=
                                                self.request.user.id)


class CourseCreate(generics.CreateAPIView):
    """
    post:
    Create course.

    Create a new course instance.
    """

    permission_classes = [api_permissions.IsTeacher, ]
    serializer_class = api_serializers.CourseSerializer

    queryset = api_models.Course.objects.all()


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Get course info.

    Return the given course.

    patch:
    Partial course update.

    Partial update the given course.

    put:
    Update course.

    Update the given course.

    delete:
    Delete course.

    Delete the given course.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.CourseRUDSerializer

    queryset = api_models.Course.objects.all()


class LectureList(generics.ListAPIView):
    """
    get:
    Get lectures list.

    Returns a list of lectures for this course.
    """

    permission_classes = [api_permissions.IsTeacherMemberOrReadOnly, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class LectureCreate(generics.CreateAPIView):
    """
    post:
    Create lecture.

    Create a new lecture instance.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Get lecture info.

    Return the given lecture.

    patch:
    Partial lecture update.

    Partial update the given lecture.

    put:
    Update lecture.

    Update the given lecture.

    delete:
    Delete lecture.

    Delete the given lecture.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.LectureSerializer

    queryset = api_models.Lecture.objects.all()


class HomeworkList(generics.ListAPIView):
    """
    get:
    Get list of homework.

    Returns a list of homeworks for this lecture.
    """

    permission_classes = [api_permissions.IsTeacherMemberOrReadOnly, ]
    serializer_class = api_serializers.HomeworkSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkCreate(generics.CreateAPIView):
    """
    post:
    Create homework.

    Create a new homework instance.
    """

    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Get homework info.

    Return the given homework.

    patch:
    Partial homework update.

    Partial update the given homework.

    put:
    Homework update.

    Update the given homework.

    delete:
    Delete homework.

    Delete the given homework.
    """

    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkRUDSerializer

    queryset = api_models.Homework.objects.all()


class HomeworkSolutionList(generics.ListAPIView):
    """
    get:
    Get list of students solution.

    Returns a list of homework solutions for this homework.
    """

    permission_classes = [api_permissions.IsTeacherMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class HomeworkStudentSolutionList(generics.ListAPIView):
    """
    get:
    Get self solutions list.

    Returns a list of student homeworks solution for this lecture.
    """

    permission_classes = [api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    def get_queryset(self):
        return api_models.HomeworkSolution.objects.filter(
            student__pk=self.request.user.id)


class HomeworkSolutionCreate(generics.CreateAPIView):
    """
    post:
    Create solution.

    Create a new homework solution instance.
    """

    permission_classes = [api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class HomeworkSolutionRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Get solution info.

    Return the given homework solution.

    patch:
    Partial solution update.

    Partial update the given homework solution.

    put:
    Update solution.

    Update the given homework solution.

    delete:
    Delete solution.

    Delete the given homework solution.
    """

    permission_classes = [api_permissions.IsStudentSolution,
                          api_permissions.IsStudentMember]
    serializer_class = api_serializers.HomeworkSolutionSerializer

    queryset = api_models.HomeworkSolution.objects.all()


class MarkList(generics.ListAPIView):
    """
    get:
    Get list of students mark.

    Returns a list of all student solutions mark for this homework.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkSerializer

    queryset = api_models.TaskMark.objects.all()


class StudentMarkList(generics.ListAPIView):
    """
    get:
    Get list of self solution marks.

    Returns a list of student solutions mark.
    """

    permission_classes = [api_permissions.IsStudentMember, ]
    serializer_class = api_serializers.MarkSerializer
    lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return api_models.TaskMark.objects.filter(
            solution=self.kwargs['homework_id'])


class CreateMark(generics.CreateAPIView):
    """
    post:
    Create mark.

    Create a new mark instance.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkSerializer

    queryset = api_models.TaskMark.objects.all()


class MarkRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Get mark info.

    Return the given mark.

    patch:
    Partial mark update.

    Partial update the given mark.

    put:
    Update mark.

    Update the given mark.

    delete:
    Delete mark.

    Delete the given mark.
    """

    permission_classes = [api_permissions.IsTeacherMember, ]
    serializer_class = api_serializers.MarkRUDSerializer

    queryset = api_models.TaskMark.objects.all()


class CommentCreate(generics.CreateAPIView):
    """
    post:
    Create comment.

    Create a new comment instance.
    """

    permission_classes = [api_permissions.IsSelfSolutionOrTeacherMember, ]
    serializer_class = api_serializers.CommentSerializer

    queryset = api_models.MarkComment.objects.all()


class CommentList(generics.ListAPIView):
    """
    get:
    Get comments list.

    Returns a list of mark comments.
    """

    permission_classes = [api_permissions.IsSelfSolutionOrTeacherMember, ]
    serializer_class = api_serializers.CommentSerializer

    queryset = api_models.MarkComment.objects.all()
