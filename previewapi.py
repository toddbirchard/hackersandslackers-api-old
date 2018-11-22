import requests
from config_loader import config


def previews(bodyhtml):
    print('bodyhtml = ', bodyhtml)
    """Replace HTML with new embeds."""
    if bodyhtml is not None:
        body = {
            'html': str(bodyhtml)
        }
        headers = {
            'Accept': 'application/json',
        }
        r = requests.post(config.gcloud_endpoint, data=body['html'].encode('utf-8'), headers=headers)
        print(r.json())
