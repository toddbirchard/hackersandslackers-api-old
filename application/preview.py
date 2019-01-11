import json


def make_preview(post):
    """Creates post preview html from link preview JSON."""

    preview_html = '<div class="link-preview"><a href="' + post['url'] + '"> \
        <div class="link-info"> \
        <div class="link-preview-image"><img src="' + post['image'] + '"></div> \
        <div class="detail-stack"> \
        <h4 class="title-desktop">' + post['title'] + '</h4> \
        <p>' + post['description'] + '</p> \ <span class="url-info"><i class="far fa-link"></i>' + post['url'] + '</span> \
        <h4 class="title-mobile">' + post['url'] + '</h4> \
        </div></div></a></div>'
    return preview_html
