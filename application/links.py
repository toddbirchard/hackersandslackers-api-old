from flask import request, make_response, render_template
from flask import current_app as app
from . import r
from . import db
from . import database
from aylienapiclient import textapi
import requests
from bs4 import BeautifulSoup


def get_alyien_extract(url):
    """Extract using Alyien API."""
    client = textapi.Client(r.get('aylien_app_id'), r.get('aylien_app_key'))
    extraction = client.Extract(url=url)
    print(extraction)
    return extraction


def make_preview(link):
    """Create post preview html from link preview JSON."""
    if link is not None:
        preview_html = '<div class="link-preview"><a href="' + str(link['url']) + '"> \
            <div class="link-info"> \
            <div class="link-preview-image"><img src="' + str(link['image']) + '"></div> \
            <div class="detail-stack"> \
            <h4 class="title-desktop">' + str(link['title']) + '</h4> \
            <p>' + str(link['description']) + '</p> \
            <span class="url-info"> \
            <i class="far fa-link"></i>' + str(link['url']) + '</span> \
            <h4 class="title-mobile">' + str(link['url']) + '</h4> \
            </div></div></a></div>'
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
        link = endpoint + tag.get('href')
        # preview_json = get_json(link)
        preview_json = get_alyien_extract(link)
        preview_embed = make_preview(preview_json)
        link_arr.append(preview_embed)
    print('link_arr = ', link_arr)
    return link_arr


@app.route('/lynx', methods=['GET', 'POST'])
def entry():
    """App Entry Point."""
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
        # preview_html = previews.make_preview(post)
        # print('postpreview = ', preview_html)
    return render_template('layout.html')


@app.route('/links', methods=['GET', 'POST'])
def main():
    """Fix website SEO, RIP Lynx Posts."""
    lynx = database.GetLynxPosts(config)
    posts_df = lynx.get_posts()
    posts_df['html'] = posts_df['html'].apply(previews, args=config.gcloud_endpoint)
