"""
This tests the homepage and extra information pages on the nav bar
"""

def test_request_main_menu_links(client):
    """ This tests the navigation bar in default page """
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_request_index(client):
    """ This ensures that the Index page gets the correct HTML response of status code 200 """
    response = client.get("/")
    assert response.status_code == 200

def test_request_git_page(client):
    """ This ensures that the Git page gets the correct HTML response of status code 200 """
    response = client.get("/Git")
    assert response.status_code == 200

def test_request_docker_page(client):
    """ This ensures that the Docker page gets the correct HTML response of status code 200 """
    response = client.get("/Docker")
    assert response.status_code == 200

def test_request_python_and_flask_page(client):
    """ This ensures that the Python/Flask page gets correct HTML response of status code 200 """
    response = client.get("/Python_Flask")
    assert response.status_code == 200

def test_request_cicd_page(client):
    """ This ensures that the CICD page gets the correct HTML response of status code 200 """
    response = client.get("/Continuous_Integration_and_Deployment")
    assert response.status_code == 200

def test_request_pylint_page(client):
    """ This ensures that the Pylint page gets the correct HTML response of status code 200 """
    response = client.get("/Pylint")
    assert response.status_code == 200

def test_request_aaa_page(client):
    """This ensures that the AAA page gets the correct HTML response of status code 200"""
    response = client.get("/Arrange_Act_Assert_Testing")
    assert response.status_code == 200

def test_request_oop_page(client):
    """This ensures that the OOP page gets the correct HTML response of status code 200"""
    response = client.get("/Object_Oriented_Programming")
    assert response.status_code == 200

def test_request_solid_page(client):
    """This ensures that the SOLID page gets the correct HTML response of status code 200"""
    response = client.get("/Solid")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This ensures that a page that doesn't exist gets
    the correct HTML response of status code 404"""
    response = client.get("/page55")
    assert response.status_code == 404
