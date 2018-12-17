import requests
from flask import g


def previews(bodyhtml):
    """Replace HTML with new embeds."""
    r = requests.post(g.gcloud_endpoint, data=bodyhtml)
    print(r.json())
