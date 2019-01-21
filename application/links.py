from flask import request, make_response, render_template
from flask import current_app as app
from logic import previews
from . import r
from . import database


@app.route('/lynx', methods=['GET', 'POST'])
def entry():
    """App Entry Point."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        }
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


@app.route('/links', methods=['GET', 'POST'])
def main():
    """Fix website SEO, RIP Lynx Posts."""
    lynx = database.GetLynxPosts(config)
    posts_df = lynx.get_posts()
    posts_df['html'] = posts_df['html'].apply(previews, args=config.gcloud_endpoint)
