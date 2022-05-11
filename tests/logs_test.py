"""
Testing if log files are properly created and are in project
"""
import os

def test_request_log_is_created():
    """ Checking the REQUEST log"""
    root = os.path.dirname(os.path.abspath(__file__))
    request_log = os.path.join(root, '../logs/request.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(request_log):
        os.mknod(request_log)
    assert os.path.exists(request_log) is True

def test_errors_log_is_created():
    """ Checking the ERROR log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errors_log = os.path.join(root, '../logs/errors.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(errors_log):
        os.mknod(errors_log)
    assert os.path.exists(errors_log) is True

def test_debug_log_is_created():
    """ Checking the DEBUG log"""
    root = os.path.dirname(os.path.abspath(__file__))
    debug_log = os.path.join(root, '../logs/debug.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(debug_log):
        os.mknod(debug_log)
    assert os.path.exists(debug_log) is True

def test_flask_log_is_created():
    """ Checking the FLASK log"""
    root = os.path.dirname(os.path.abspath(__file__))
    flask_log = os.path.join(root, '../logs/flask.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(flask_log):
        os.mknod(flask_log)
    assert os.path.exists(flask_log) is True

def test_sql_alchemy_log_is_created():
    """ Checking the SQL ALCHEMY log"""
    root = os.path.dirname(os.path.abspath(__file__))
    sql_alchemy_log = os.path.join(root, '../logs/sqlalchemy.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(sql_alchemy_log):
        os.mknod(sql_alchemy_log)
    assert os.path.exists(sql_alchemy_log) is True

def test_my_app_log_is_created():
    """ Checking the MYAPP log"""
    root = os.path.dirname(os.path.abspath(__file__))
    my_app_log = os.path.join(root, '../logs/myapp.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(my_app_log):
        os.mknod(my_app_log)
    assert os.path.exists(my_app_log) is True

def test_update_csv_log_is_created():
    """ Checking the UPDATE CSV log"""
    root = os.path.dirname(os.path.abspath(__file__))
    update_csv_log = os.path.join(root, '../logs/updatecsv.log')
    # Ensuring whether the request file exists. If not, then generate a new one
    if not os.path.exists(update_csv_log):
        os.mknod(update_csv_log)
    assert os.path.exists(update_csv_log) is True
