from flask import request, make_response, render_template
from flask import current_app as app
from . import r
from . import db
from . import database
import requests
from bs4 import BeautifulSoup
import json
import pprint


def get_alyien_extract(url):
    """Extract using Alyien API."""
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


def get_alyien_summary(url):
    """Extract using Alyien API."""
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


def make_preview(preview_obj):
    """Create post preview html from link preview JSON."""
    if preview_obj is not None:
        preview_html = '<div class="link-preview"> \
                            <a href="' + str(preview_obj['url']) + '"> \
                                <div class="link-info"> \
                                    <div class="link-preview-image"> \
                                        <img src="' + str(preview_obj['image']) + '"></div> \
                                        <div class="detail-stack"> \
                                            <h4 class="title-desktop">' + str(preview_obj['title']) + '</h4> \
                                            <p>' + str(preview_obj['summary']) + '</p> \
                                            <h4 class="title-mobile">' + str(preview_obj['url']) + '</h4> \
                                            <span class="url-info"><i class="far fa-link"></i>' + str(preview_obj['url']) + '</span> \
                                        </div> \
                                    </div> \
                                </a> \
                            </div>'
    return preview_html


def get_links(url):
    """Extract links from url."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    endpoint = r.get('endpoint')
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    tags = soup.select('.post-content a')
    link_arr = []
    for tag in tags:
        link = tag.get('href')
        preview_obj = get_alyien_extract(link)
        summary = get_alyien_summary(link)
        preview_obj['summary'] = summary
        preview_obj['url'] = link
        preview_obj['lynxorigin'] = url
        preview_obj.pop('article', None)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(preview_obj)
        preview_embed = make_preview(preview_obj)
        link_arr.append(preview_embed)
    print('link_arr = ', link_arr)
    return link_arr


@app.route('/lynx', methods=['GET', 'POST'])
def entry():
    """App Entry Point."""
    print('HERP', r.get('aylien_app_id'))
    print('DERP', r.get('aylien_app_key'))
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        }
    uri = r.get('uri')
    '''query = r.get('query')
    query_like = r.get('query_like')'''
    domain = r.get('domain')
    post_database = database.LynxData()
    posts = post_database.fetch_records()
    for post in posts:
        url = domain + post['slug']
        link_embeds = get_links(url)
        page_html = ''.join(str(x) for x in link_embeds)
        print('page_html = ', page_html)
        post_database.update_post(uri, post['slug'], page_html)
        preview_html = make_preview(post)
        print('postpreview = ', preview_html)
    return render_template('layout.html')
