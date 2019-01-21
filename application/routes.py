from flask import current_app as app
from flask import render_template, make_response, request
import json
import requests
from . import r
from . import database
from . import previews


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


@app.route('/medium/me', methods=['GET'])
def get_user_details():
    """Get details of current user."""
    endpoint = r.get('medium_endpoint_me')
    token = r.get('token')
    headers = {
        'Authorization': r.get('token'),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    req = requests.get(url=endpoint, headers=headers)
    response = req.content
    print(response)
    return make_response(response, 200)


@app.route('/medium/publish', methods=['POST'])
def publish_post():
    """Publish post to medium."""
    post_data = request.data
    data_dict = json.loads(post_data)
    title = data_dict['title']
    content = data_dict['content']
    contentFormat = data_dict['contentFormat']
    tags = data_dict['tags']
    token = r.get('token')
    publication = r.get('publication')
    endpoint = 'https://api.medium.com/v1/publications/' + publication + '/posts'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    data = {
        "title": title,
        "contentFormat": "html",
        "content": content,
        "tags": tags,
        "publishStatus": "draft",
    }
    req = requests.post(url=endpoint, headers=headers, data=json.dumps(data))
    response = req.text
    return make_response(response, 200)
