from db import GetLynxPosts
from config_loader import config
from previewapi import previews


def main():
    """Fix website SEO, RIP Lynx Posts."""
    lynx = GetLynxPosts(config)
    posts_df = lynx.get_posts()
    posts_df['html'] = posts_df['html'].apply(previews)


main()
