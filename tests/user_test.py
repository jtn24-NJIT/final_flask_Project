"""
This file is to test the users table
"""
import logging
from app import db
from app.db.models import User, Transaction

def test_adding_user(application):
    """ Adding a test user to db """
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        # Showing how to add a record
        # First, create a record
        user = User('keith@webizly.com', 'testtest', 1)
        # Add it to get ready to be committed
        db.session.add(user)
        # Finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        # Asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        # This is how you get a related record ready for insert
        user.transactions = [Transaction(500.0,"CREDIT"), Transaction(-120.5, "DEBIT")]
        # Commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        transaction1 = Transaction.query.filter_by(AMOUNT=500.0).first()
        assert transaction1.AMOUNT == 500.0
        # changing the amount of transaction 1
        transaction1.AMOUNT = 600.25
        db.session.commit()
        transaction2 = Transaction.query.filter_by(AMOUNT=-120.5).first()
        assert transaction2.AMOUNT == -120.5
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
