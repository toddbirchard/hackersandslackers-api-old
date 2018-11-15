from db import get_lynx_posts
from config_loader import config


def main():
    """Fix website SEO, RIP Lynx Posts."""
    lynx_table = get_lynx_posts(config.uri)
    posts = lynx_table.get_posts()
    for post in posts:
        print(post)


main()
