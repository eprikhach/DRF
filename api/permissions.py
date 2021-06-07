from rest_framework import permissions
from .models import Course, HomeworkSolution


class IsTeacher(permissions.BasePermission):
    """Custom permission class."""

    def has_permission(self, request, view):
        """Returns True if user is a teacher.

        :param request: request
        :param view: view
        :return: boolean
        """

        user = request.user

        if user.is_staff:
            return True

        if user.is_authenticated and user.user_status == 'T':
            return True

        return False


class IsTeacherMember(permissions.BasePermission):
    """Custom permission class."""

    def has_permission(self, request, view):
        """Returns True if user is in teacher field.

        :param request: request
        :param view: view
        :return: boolean
        """

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
    """Custom permission class."""

    def has_permission(self, request, view):
        """Return true if user is in students field.

        :param request: request
        :param view: view
        :return: boolean
        """

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
    """Custom permission class."""

    def has_permission(self, request, view):
        """Returns True if solution was created by this user.

        :param request: request
        :param view: view
        :return: boolean
        """

        if request.user.is_staff:
            return True

        if view.kwargs.get('pk'):
            return HomeworkSolution.objects.filter(
                Student=request.user.pk,
                id=view.kwargs['pk'])

        return False


class IsTeacherMemberOrReadOnly(permissions.BasePermission):
    """Custom permission class."""

    def has_permission(self, request, view):
        """Returns True if user is in teachers field or method is safe.

        :param request: request
        :param view: view
        :return: boolean
        """

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
    """Custom permission class."""

    def has_permission(self, request, view):
        """Returns True if user is solution owner or in teachers field.

        :param request:
        :param view:
        :return:
        """
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
