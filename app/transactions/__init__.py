import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Transaction
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__,
                        template_folder='templates')

@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def browse_transactions(page):
    page = page
    per_page = 10000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)

@transactions.route('/transactions_datatables/', methods=['GET'])
def browse_transactions_datatables():
    data = Transaction.query.filter_by(user_id=current_user.id)
    try:
        return render_template('browse_transactions_datatables.html',data=data )
    except TemplateNotFound:
        abort(404)

@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transaction_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        current_user.balance = 0.00
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                current_user.balance += float(row['AMOUNT'])
                current_user.transactions.append(Transaction(row['AMOUNT'],row['TYPE']))
                db.session.commit()
        return redirect(url_for('transactions.browse_transactions_datatables'))

    try:
        return render_template('upload_transactions.html', form=form)
    except TemplateNotFound:
        abort(404)