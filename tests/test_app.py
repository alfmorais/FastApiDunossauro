def test_root_success(client):
    expected_result = {'message': 'Olá Mundo!'}

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == expected_result


def test_create_user_success(client):
    expected_result = {
        'id': 1,
        'username': 'alfredneto',
        'email': 'alfredneto@email.com',
    }
    payload = {
        'username': 'alfredneto',
        'email': 'alfredneto@email.com',
        'password': '123456',
    }

    response = client.post('/users/', json=payload)

    assert response.status_code == 201
    assert response.json() == expected_result


def test_read_users_success(client):
    expected_result = {
        'users': [
            {
                'id': 1,
                'username': 'alfredneto',
                'email': 'alfredneto@email.com',
            }
        ]
    }

    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == expected_result


def test_update_user_success(client):
    expected_result = {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }
    payload = {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'mynewpassword',
    }

    response = client.put('/users/1', json=payload)

    assert response.status_code == 200
    assert response.json() == expected_result


def test_update_user_error(client):
    expected_result = {'detail': 'User not found'}
    payload = {
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'mynewpassword',
    }

    response = client.put('/users/99', json=payload)

    assert response.status_code == 404
    assert response.json() == expected_result


def test_delete_user_success(client):
    expected_result = {'detail': 'User deleted'}
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == expected_result


def test_delete_user_error(client):
    expected_result = {'detail': 'User not found'}
    response = client.delete('/users/99')

    assert response.status_code == 404
    assert response.json() == expected_result
