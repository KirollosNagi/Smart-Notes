import pytest
from django.contrib.auth.models import User
from .factories import UserFactory

@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.login(username=user.username, password='password') 
    return user

def test_home_endpoint_returns_a_welcome_page(client):
    response = client.get(path='/')
    assert 200 == response.status_code
    assert 'Welcome to smart notes!' in str(response.content)

def test_signup_endpoint_returns_from_for_unauthenticated_user(client):
    response = client.get(path='/signup')
    assert 200 == response.status_code
    assert 'home/register.html' in response.template_name
    assert 'Enter the same password as before, for verification' in str(response.content)

@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client, logged_user):
    '''
      When a user is authenticated and try to access the 
      signup page, they are redirected to the list of their notes.
    '''

    assert logged_user.is_authenticated

    response = client.get(path='/signup', follow=True)
    print(type(response))
    assert 200 == response.status_code
    assert 'note/note_list.html' in response.template_name
