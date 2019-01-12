import requests
from flask import r


def previews(bodyhtml):
    """Replace HTML with new embeds."""
    req = requests.post(r.get('endpoint'), data=bodyhtml)
    print(req.json())
