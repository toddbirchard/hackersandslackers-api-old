import requests
from config_loader import config


def previews(bodyhtml):
    """Replace HTML with new embeds."""
    r = requests.post(config.gcloud_endpoint, data=bodyhtml)
    print(r.json())
