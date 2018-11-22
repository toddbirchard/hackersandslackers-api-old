import requests


def previews(bodyhtml):
    """Replace HTML with new embeds."""
    r = requests.post(config.gcloud_endpoint, data=bodyhtml)
    print(r.json())
