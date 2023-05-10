import pytest
from app import schemas

# GET posts tests
def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOUT(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
   

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/888888")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")

    post = schemas.PostOUT(**res.json())
    
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title

#CREATE posts tests
@pytest.mark.parametrize("title, content, published", [
    ("test new title", "test new content", True),
    ("newyork new title", "newyork new content", True),
    ("brasil ocean", "ocean content", False)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json = {"title": title, "content": content, "published": published})

    created_Post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_Post.title == title
    assert created_Post.content == content
    assert created_Post.published == published
    assert created_Post.owner_id == test_user['id']

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts/", json = {"title": "arbitary title", "content": "test content"})

    created_Post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_Post.title == "arbitary title"
    assert created_Post.content == "test content"
    assert created_Post.published == True
    assert created_Post.owner_id == test_user['id']

def test_unauthorized_user_create_post(client, test_posts, test_user):
    res = client.post("/posts/", json = {"title": "arbitary title", "content": "test content"})
    assert res.status_code == 401

#DELETE posts test
def test_unauthorized_user_delete_post(client, test_posts, test_user):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204

def test_delete_non_existing_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/90090908980909809099809809809009")
    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403

#UPDATE post test
def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated test title test", 
        "content": "updated test content test",
        "id": test_posts[0].id
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']

def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
    data = {
        "title": "updated test title test", 
        "content": "updated test content test",
        "id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403

def test_unauthorized_user_update_post(client, test_posts, test_user):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_update_non_existing_post(authorized_client, test_user, test_posts):
    data = {
        "title": "updated test title test", 
        "content": "updated test content test",
        "id": test_posts[3].id
    }
    res = authorized_client.put(f"/posts/90090908980909809099809809809009", json=data)
    assert res.status_code == 404