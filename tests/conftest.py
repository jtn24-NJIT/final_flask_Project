"""This makes the test configuration setup"""
import os
import pytest

from flask import current_app

from app import create_app, User
from app.db import db

@pytest.fixture()
def application():
    """This makes the appplication itself"""
    os.environ['FLASK_ENV'] = 'testing'
    application = create_app()
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        # This line drops the database tables after the test runs, ensuring any records made are deleted
        db.drop_all()
    return application

@pytest.fixture()
def add_user(application):
    """ Adding a user to the application's database """
    with application.app_context():
        # New record, username, password and not admin
        user = User('keith@webizly.com', 'testtest', 0)
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def client(application):
    """ This makes the http client """
    return application.test_client()

@pytest.fixture()
def runner(application):
    """ This makes the task runner """
    return application.test_cli_runner()
