"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os
import pytest
import app

#this is a good tutorial I used to fix this code to do database testing.
#https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/

@pytest.fixture()
def application():
    """This makes the app"""
    #you need this one if you want to see whats in the database
    #os.environ['FLASK_ENV'] = 'development'
    #you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = app.create_app()

    with application.app_context():
        app.db.create_all()
        yield application
        app.db.session.remove()
        #drops the database tables after the test runs
        #db.drop_all()

@pytest.fixture()
def add_user(application):
    """ Adding a user to the application's database """
    with application.app_context():
        #new record
        user = app.User('keith@webizly.com', 'testtest', 0)
        app.db.session.add(user)
        app.db.session.commit()

@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
