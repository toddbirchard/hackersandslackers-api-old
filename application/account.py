import os
import sys
import json
import urllib.request as urllib
from flask import Flask, Blueprint, request, make_response
from flask import current_app as app
import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
from . import db
from . import models


accounts_blueprint = Blueprint('accounts', __name__)

@app.route("/account/emails/welcome", methods=["POST"])
def welcome_mailer():
    """Send welcome email."""
    api_key = os.environ.get("SENDGRID_API_KEY")
    sg = sendgrid.SendGridAPIClient(apikey=api_key)
    if request.method == "POST":
        post_data = request.data
        data_dict = json.loads(post_data)
        print('data_dict = ', data_dict)
        sys.stdout.flush()
        subscribers = data_dict['subscribers']
        for subscriber in subscribers:
            to_email = Email(subscriber['email'])
            from_email = Email(os.environ["FROM_EMAIL"])
            subject = "Welcome to Hackers & Slackers"
            print("subscriber['email'] = ", subscriber['email'])
            sys.stdout.flush()
            mail = Mail(from_email, subject, to_email)
            mail.template_id = os.environ["TEMPLATE_ID"]
            try:
                response = sg.client.mail.send.post(request_body=mail.get())
                return make_response('it worked?', 200)
            except urllib.HTTPError as e:
                print(e.read())
                sys.stdout.flush()
                print(response.status_code)
                sys.stdout.flush()
                print(response.body)
                sys.stdout.flush()
                print(response.headers)
                sys.stdout.flush()
                return make_response(e.read(), 500)


def get_gravatar(email):
    """Encrypt email for gravatar id."""
    grav = Gravatar(str(email))
    grav.get_image()
    return str(grav).encode("utf-8")


@app.route('/account/createrecord', methods=['POST'])
def create_acount():
    """Prepare a new user account for the subscriber."""
    post_data = request.data
    data_dict = json.loads(post_data)
    name = data_dict['name']
    email = data_dict['email']
    grav = get_gravatar(email)   # Derive Gravatar from Email
    user = models.Reader(name, email, grav)
    session = db.LynxData.open_session()
    session.add(user)
    session.commit()
    # Insert DB record
    # new_account = UserAccounts(username, email, grav)
    # new_account.create_account
    return make_response(user, 200)
