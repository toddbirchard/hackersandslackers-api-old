from flask import Blueprint, make_response, g
import json

preview_blueprint = Blueprint('preview', __name__, template_folder='templates', static_folder='static')
headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
    }


@preview_blueprint.route('/', methods=['GET', 'POST'])
def entry():
    previews = 'test response'
    response_body = json.dumps(previews)
    return make_response(str(response_body), 200, headers)
