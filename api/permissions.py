from loguru import logger
from rest_framework import permissions
from .models import Course, HomeworkSolution


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_staff:
            return True

        if user.is_authenticated and user.user_status == 'T':
            return True

        return False


class IsTeacherMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        user = request.user
        view = view.kwargs

        if user.is_staff:
            return True
        if view.get('course_id'):
            course_id = view['course_id']
            return Course.objects.filter(pk=course_id,
                                         Teachers__id=user.pk)
        elif view.get('pk'):
            course_id = view['pk']
            return Course.objects.filter(pk=course_id,
                                         Teachers__id=user.pk)

        return False


class IsStudentMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user
        view = view.kwargs

        if user.is_staff:
            return True

        if view.get('course_id'):
            course_id = view['course_id']
            return Course.objects.filter(pk=course_id,
                                         Students__id=user.pk)

        return False


class IsStudentSolution(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        if view.kwargs.get('pk'):
            return HomeworkSolution.objects.filter(
                Student=request.user.pk,
                id=view.kwargs['pk'])

        return False


class IsTeacherMemberOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if view.get('course_id'):
            course_id = view['course_id']
            return Course.objects.filter(pk=course_id,
                                         Teachers__id=user.pk)

        return False


class IsSelfSolutionOrTeacherMember(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        view = view.kwargs

        if user.is_staff:
            return True

        if view.get('solution_id'):
            course_id = view['course_id']

            if HomeworkSolution.objects.filter(Student=user.pk,
                                               id=view['solution_id']):

                return True

            elif Course.objects.filter(pk=course_id,
                                       Teachers__id=user.pk):

                return True

        return False
