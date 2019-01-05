from flask import current_app as app
from flask import Blueprint, render_template, g
from flask_assets import Bundle, Environment
import json
from . import redis_store
from . import db

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

main_blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static', root_path='application')

assets = Environment(app)
js = Bundle('js/bin/*.js', filters='jsmin', output='dist/packed.js')
scss = Bundle('scss/*.scss', filters='libsass', output='dist/all.css')
assets.register('scss_all', scss)
assets.register('js_all', js)



@main_blueprint.route('/', methods=['GET', 'POST'])
def entry():
    # readers = models.Readers.query.filter_by(username='john').all()
    # base_url = redis_store.get('ENDPOINT')
    uri = redis_store.get('uri').decode('utf-8')
    query = redis_store.get('query').decode('utf-8')
    querylike = redis_store.get('querylike').decode('utf-8')
    print('uri = ', uri)
    database = db.LynxData(uri, query, querylike)
    print('database.uri = ', database.uri)
    records = database.records
    return render_template('layout.html', results=records)
