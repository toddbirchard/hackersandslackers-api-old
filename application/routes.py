from flask import current_app as app
from flask import make_response
import json
from . import models
from . import redis_store


headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
    }


@app.route('/', methods=['GET', 'POST'])
def entry():
    readers = models.Readers.query.filter_by(username='todd').all()
    print(readers)
    return make_response(str('readers'), 200, headers)
