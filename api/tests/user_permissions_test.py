import pytest


from api.models import User
from django.urls import reverse
from pytest_drf import APIViewTest, AsUser, Returns200, UsesGetMethod, \
    Returns403, UsesPostMethod, Returns201
from pytest_lambda import lambda_fixture, static_fixture

alice = lambda_fixture(
    lambda: User.objects.create(
        id=2,
        username='alice',
        password='',
        email='alice@ali.ce',
        user_status='S',
        is_active=True
    ))

alice_teacher = lambda_fixture(
    lambda: User.objects.create(
        id=3,
        username='alice_teacher',
        password='',
        email='alice@ali.ce',
        user_status='T',
        is_active=True
    ))


@pytest.mark.django_db
class TestAboutMe(APIViewTest,
                  UsesGetMethod,
                  Returns200,
                  AsUser('alice')):
    url = lambda_fixture(lambda: reverse('user-list'))

    def test_it_returns_profile(self, json):
        expected = [{
            'id': 2,
            'password': '',
            'email': 'alice@ali.ce',
            'username': 'alice',
            'user_status': 'S',
        }]
        actual = json
        assert expected == actual


@pytest.mark.django_db
class TestCoursesWithStudentRole(APIViewTest,
                                 UsesGetMethod,
                                 Returns200,
                                 AsUser('alice')):

    url = lambda_fixture(lambda: reverse('TeacherCourseList'))

    def test_is_teacher_courses_empty(self, json):
        expected = []

        actual = json

        assert expected == actual


@pytest.mark.django_db
class TestCoursesCreateWithStudentRole(APIViewTest,
                                       UsesPostMethod,
                                       Returns403,
                                       AsUser('alice')):

    url = lambda_fixture(lambda: reverse('CreateCourse'))
    data = static_fixture({'name': 'Test course',
                           'description': 'Test description'})

    def test_is_students_can_create_course(self, json):
        expected = {'detail': 'You do not have permission to perform this '
                              'action.'}

        assert expected == json


@pytest.mark.django_db
class TestCoursesCreateWithTeacherRole(APIViewTest,
                                       UsesPostMethod,
                                       Returns201,
                                       AsUser('alice_teacher'),
                                       ):

    url = lambda_fixture(lambda: reverse('CreateCourse'))
    data = static_fixture({'name': 'Test course',
                           'description': 'Test description'})

    def test_is_teachers_can_create_course(self, json):

        expected = {'name': 'Test course',
                    'description': 'Test description'}

        assert [expected['name'], expected['description']] ==\
               [json['name'], json['description']]
