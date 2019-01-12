from flask import current_app as app
from flask import Blueprint, render_template, g
import json
from . import r
from . import database
from . import previews

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

main_blueprint = Blueprint('main', __name__, template_folder='templates', static_folder='static', root_path='application')

'''assets = Environment(app)
js = Bundle('js/bin/*.js', filters='jsmin', output='dist/packed.js')
scss = Bundle('scss/*.scss', filters='libsass', output='dist/all.css')
assets.register('scss_all', scss)
assets.register('js_all', js)'''



@main_blueprint.route('/', methods=['GET', 'POST'])
def entry():
    """App Entry Point."""
    uri = r.get('uri')
    query = r.get('query')
    query_like = r.get('query_like')
    domain = r.get('domain')
    post_database = database.LynxData(uri, query, query_like)
    posts = post_database.records
    for post in posts:
        url = domain + post['slug']
        link_embeds = previews.get_links(url)
        page_html = ''.join(str(x) for x in link_embeds)
        print('page_html = ', page_html)
        post_database.update_post(uri, post['slug'], page_html)
        # preview_html = previews.make_preview(post)
        # print('postpreview = ', preview_html)
    return render_template('layout.html')
