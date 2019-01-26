from mixpanel import Mixpanel
from . import r
import json
import requests
from flask import current_app as app
from flask import render_template, make_response, request
import pandas as pd


mp = Mixpanel(r.get('mixpanel_api_token'))


@app.route('/mixpanel/newaccount', methods=['GET', 'POST'])
def mixpanel_new_account():
    """Create a new person in mixpanel."""
    post_data = request.data
    data_dict = json.loads(post_data)
    email = data_dict['email']
    name = data_dict['name']
    mp.people_set(email, {'$name': name, '$email': email})
    return make_response(str(email), 200)


@app.route('/mixpanel/deleteaccounts', methods=['GET'])
def mixpanel_delete_account():
    """Publish post to medium."""
    users_df = pd.read_csv('data/people.csv')
    for index, row in users_df.iterrows():
        mp.people_delete(row['id'])
        print(row['id'])
    return make_response('done.', 200)
