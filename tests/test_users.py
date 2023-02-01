import pytest
from jose import jwt
from app import schemas
from app.config import settings



# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello world!'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "test@gmail.com", "password": "testpass123"})
    
    # ** added on res.json in order to unpack dictionary, to be in correct format 
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrong@gmail.com', 'testpass123', 403),
    ('test@gmail.com', 'wrongpass', 403),
    ('wrong@gmail.com', 'wrongpass', 403),
    ('test@gmail.com', None , 422),
    (None, 'testpass123', 422)
])
def test_failed_login(test_user, client, email, password, status_code):
    res = client.post("login", data= {"username": email, "password": password})

    assert res.status_code == status_code
    #assert res.json().get('detail') == 'Invalid Credentials'