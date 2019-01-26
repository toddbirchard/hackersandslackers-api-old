import json
import requests
from flask import current_app as app
from flask import render_template, make_response, request
from . import r
from . import db


@app.route('/medium/me', methods=['GET'])
def get_user_details():
    """Get details of current user."""
    endpoint = r.get('medium_endpoint_me')
    token = r.get('medium_token')
    headers = {
        'Authorization': r.get('medium_token'),
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
    tags = data_dict['tags']
    token = r.get('medium_token')
    publication = r.get('medium_publication')
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
