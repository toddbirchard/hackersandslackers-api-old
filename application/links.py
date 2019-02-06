from flask import request, make_response, render_template
from flask import current_app as app
from . import r
from . import db
from . import database
import requests
from bs4 import BeautifulSoup
import json
import pprint
from datetime import datetime as dt


def sanitize_data(obj):
    """Sanitizes link embed data to be human-readable."""
    # Clean URL to be easily readable.
    displayurl = obj['url'].split('://')[0]
    displayurl = displayurl.replace('www.', '')
    obj['displayurl'] = displayurl
    # Reformat date
    published = dt.strftime(obj['publihDate'], '%m/%d/%Y %p')
    obj['publishDate'] = published
    # Format tags
    tags = [lambda x: '#' + x.replace(' ', ''), obj['tags']]
    obj['tags'] = tags
    return obj


def get_aylien_extract(url):
    """Extract url information using aylien API."""
    headers = {
        'X-AYLIEN-TextAPI-Application-Key': r.get('aylien_app_key'),
        'X-AYLIEN-TextAPI-Application-ID': r.get('aylien_app_id'),
        'Content-Type': 'application/json'
    }
    params = {
        'url': url,
        'best_image': 'true'
    }
    base_url = 'https://api.aylien.com/api/v1/extract'
    req = requests.get(base_url, headers=headers, params=params)
    return req.json()


def get_aylien_summary(url):
    """Generate a 3-sentence summary of the URL using Aylien."""
    headers = {
        'X-AYLIEN-TextAPI-Application-Key': r.get('aylien_app_key'),
        'X-AYLIEN-TextAPI-Application-ID': r.get('aylien_app_id')
    }
    params = {
        'url': url,
        'sentences_number': 3
    }
    base_url = 'https://api.aylien.com/api/v1/summarize'
    req = requests.get(base_url, headers=headers, params=params)
    sentences = req.json()['sentences']
    summary = ' '.join(sentences)
    return summary


def make_preview(linkpreview):
    """Create post preview HTML from link preview JSON."""
    if linkpreview is not None:
        return render_template('linkpreview.html', data=linkpreview)
    return None


def generate_url_metadata(url, posturl):
    """Create link preview metadata object.

    1. Create extract using Aylien Extract API.
    2. Generate URL summary using Aylien Summary API.
    3. Add simple metadata to object.
    4. Sanitize data.
    5. Create HTML embed using Jinja Template.
    6. Return embed.
    """
    preview_obj = get_aylien_extract(url)
    summary = get_aylien_summary(url)
    preview_obj['summary'] = summary
    preview_obj['url'] = url
    preview_obj['lynxorigin'] = posturl
    preview_obj.pop('article', None)
    preview_obj = sanitize_data(preview_obj)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(preview_obj)
    preview_embed = make_preview(preview_obj)
    return preview_embed


def get_links(url):
    """Extract links from url."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    # endpoint = r.get('endpoint')
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    htmltags = soup.select('.post-content a')
    link_arr = []
    for tag in htmltags:
        link = tag.get('href')
        preview = generate_url_metadata(link, url)
        link_arr.append(preview)
    print('link_arr = ', link_arr)
    return link_arr


@app.route('/linkembed', methods=['GET', 'POST'])
def linkembed():
    """Link embed entry point."""
    uri = r.get('uri')
    domain = r.get('domain')
    post_database = database.LynxData()
    posts = post_database.fetch_records()
    for post in posts:
        posturl = domain + post['slug']
        link_embeds = get_links(post)
        preview = generate_url_metadata(post, posturl)
        # page_html = ''.join(str(x) for x in link_embeds)
        # print('page_html = ', page_html)
        # post_database.update_post(uri, post['slug'], page_html)
        print('preview = ', preview)
    return render_template('layout.html')
