"""
Tests if a new user can be registered and logged into website
"""
import logging
from app.auth.forms import login_form, register_form

def test_user_registration(application):
    """ Test user registration and log it """
    log = logging.getLogger("myApp")
    log.info("User REGISTER test")
    with application.test_request_context():
        form = register_form()
        form.email.data = "pop@gmail.com"
        form.password.data = "poPer@50*"
        form.confirm.data = "poPer@50*"
        assert form.validate

def test_user_login(application):
    """ Test user login and log it """
    log = logging.getLogger("myApp")
    log.info("User LOGIN test")
    with application.test_request_context():
        form = login_form()
        form.email.data = "pop@gmail.com"
        form.password.data = "poPer@50*"
        assert form.validate
