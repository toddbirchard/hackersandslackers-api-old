from flask import current_app as app
from flask import make_response
import json
from . import models
from . import redis_store


headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
    }


@app.route('/', methods=['GET', 'POST'])
def entry():
    readers = models.Readers.query.filter_by(username='john').all()
    print(readers)
    print(redis_store.endpoint)
    return make_response(str('readers'), 200, headers)
