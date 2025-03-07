import pytest

from django.contrib.auth.models import User
from notes.models import Notes

@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client):
    user = User.objects.create_user(username='user', password='password')
    client.login(username=user.username, password='password')

    note = Notes.objects.create(title='An Interesting title', text='This is an interesting note', user=user)
    second_note = Notes.objects.create(title='Another Interesting title', text='This is another interesting note', user=user)

    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content = str(response.content)
    assert 'An Interesting title' in content
    assert 'Another Interesting title' in content
    assert 2 == content.count('<h3>')

@pytest.mark.django_db
def test_list_endpoint_only_list_notes_from_authenticated_user(client):
    user1 = User.objects.create_user(username='user1', password='password')
    user2 = User.objects.create_user(username='user2', password='password')

    Notes.objects.create(title='User2 Note', text='User 1 is not supposed to see this', user=user2)

    client.login(username=user1.username, password='password')

    note = Notes.objects.create(title='An Interesting title', text='This is an interesting note', user=user1)
    second_note = Notes.objects.create(title='Another Interesting title', text='This is another interesting note', user=user1)

    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content = str(response.content)
    assert 'An Interesting title' in content
    assert 'Another Interesting title' in content
    assert 'User2 Note' not in content
    assert 2 == content.count('<h3>')
