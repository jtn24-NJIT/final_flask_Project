"""
File to create the database and/or ensure it is there
"""
import os
from click.testing import CliRunner
from app import create_database
runner = CliRunner()

def test_create_database():
    """ Creating the database, ensuring exit code for response is 0 & checking filepath """
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) is True
