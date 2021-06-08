import pytest

from api.models import User
from django.urls import reverse
from pytest_drf import APIViewTest, AsUser, Returns200, UsesPostMethod
from pytest_lambda import lambda_fixture

alice = lambda_fixture(
    lambda: User.objects.create(
        username='alice',
        first_name='Alice',
        last_name='Innchains',
        email='alice@ali.ce',
    ))


@pytest.mark.django_db
class TestAboutMe(
    APIViewTest,
    UsesPostMethod,
    Returns200,
    AsUser('alice'),
):
    url = lambda_fixture(lambda: reverse('/auth/users/'))

    def test_it_returns_profile(self, json):
        expected = {
            'username': 'alice',
            'first_name': 'Alice',
            'last_name': 'Innchains',
            'email': 'alice@ali.ce',
        }
        actual = json
        assert expected == actual