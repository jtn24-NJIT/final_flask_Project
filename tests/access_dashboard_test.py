"""
Testing the dashboard page as an admin and non-admin user to ensure correct response codes
"""
from flask_login import FlaskLoginClient

from app import db
from app.db.models import User

def test_dashboard_access_as_admin(application):
    """ This test ensures that the dashboard can be accessed with an admin user """
    application.test_client_class = FlaskLoginClient
    user = User('bob@gmail.com', 'passwoRD@91!', 1)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'bob@gmail.com'

    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert b'bob@gmail.com' in response.data
        assert response.status_code == 200

def test_dashboard_access_as_non_admin(application):
    """ This test ensures that the dashboard can NOT be accessed with a NON-admin user """
    application.test_client_class = FlaskLoginClient
    with application.test_client(user=None) as client:
        response = client.get('/dashboard')
        # Return a 302/redirect response code
        assert response.status_code == 302
