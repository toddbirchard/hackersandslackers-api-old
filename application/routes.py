from flask import current_app as app
from flask import Blueprint, render_template, g
from flask_assets import Bundle, Environment
import json
from . import r
from . import db
from preview import make_preview

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
    # base_url = redis_store.get('ENDPOINT')
    uri = r.get('uri').decode('utf-8')
    query = r.get('query').decode('utf-8')
    querylike = r.get('querylike').decode('utf-8')
    database = db.LynxData(uri, query, querylike)
    posts = database.records
    for post in posts:
        make_preview(post)
    return render_template('layout.html', results=posts)
