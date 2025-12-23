import pytest
from izzoApp import create_app
from izzoApp.utils.db import db
from izzoApp.models.role import Role


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()

         # 🔥 Seed mínimo obligatorio
        admin_role = Role(name="admin")
        db.session.add(admin_role)
        db.session.commit()

        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header(client):
    # register
    client.post("/auth/register", json={
        "email": "admin@test.com",
        "password": "123456",
        "role": "admin"
    })

    # login
    res = client.post("/auth/login", json={
        "email": "admin@test.com",
        "password": "123456"
    })

    token = res.json["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }
