from flask import current_app as app
from flask import Blueprint, render_template, g
from flask_assets import Bundle, Environment
import json
from db import LynxData
from . import models
from . import redis_store


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
scss.build()
js.build()


@main.route('/', methods=['GET', 'POST'])
def entry():
    # readers = models.Readers.query.filter_by(username='john').all()
    base_url = app.Config.getConfigValue('BASE_URL')
    sqlalchemy_database_uri = app.Config.getConfigValue('SQLALCHEMY_DATABASE_URI')
    query = app.Config.getConfigValue('POST_QUERY')
    querylike = app.Config.getConfigValue('QUERY_LIKE')
    database = LynxData(base_url, sqlalchemy_database_uri, query, querylike)
    records = database.fetch_records()
    return render_template('layout.html', results=records)
