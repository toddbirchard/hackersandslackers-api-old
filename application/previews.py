import json
import requests
from bs4 import BeautifulSoup
from . import r


def get_json(link):
    """Replace HTML with new embeds."""
    req = requests.post(link)
    return req.json()


def make_preview(link):
    """Creates post preview html from link preview JSON."""
    preview_html = '<div class="link-preview"><a href="' + str(link['url']) + '"> \
        <div class="link-info"> \
        <div class="link-preview-image"><img src="' + str(link['image']) + '"></div> \
        <div class="detail-stack"> \
        <h4 class="title-desktop">' + str(link['title']) + '</h4> \
        <p>' + str(link['description']) + '</p> \ <span class="url-info"><i class="far fa-link"></i>' + str(link['url']) + '</span> \
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
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    tags = soup.select('.post-content a')
    link_arr = []
    for tag in tags:
        link = tag.get('href')
        preview_json = get_json(link)
        print('link = ', link)
        preview_embed = make_preview(preview_json)
        print('preview_embed = ', preview_embed)
        link_arr.append(preview_embed)
    return link_arr
