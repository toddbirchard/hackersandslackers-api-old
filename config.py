import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.environ["TESTING"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]
    SESSION_TYPE = os.environ["SESSION_TYPE"]
    REDIS_URL = os.environ["REDIS_URL"]

    # Endpoint
    ENDPOINT = os.environ["PREVIEW_ENDPOINT"]
    DOMAIN = os.environ["DOMAIN"]

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_ECHO = os.environ["SQLALCHEMY_ECHO"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]

    # Queries
    POST_QUERY = os.environ["POST_QUERY"]
    QUERY_LIKE = os.environ["QUERY_LIKE"]

    # Apisentris
    ACCESS_TOKEN = os.environ["APISENTRIS_ACCESS_TOKEN"]
    CLIENT_ID = os.environ["APISENTRIS_CLIENT_ID"]
    HEADER_CONTENT_TYPE = os.environ["APISENTRIS_HEADER_CONTENT_TYPE"]

    # Ghost to Medium
    MEDIUM_TOKEN = os.environ['MEDIUM_TOKEN']
    MEDIUM_CLIENT_ID = os.environ['MEDIUM_CLIENT_ID']
    MEDIUM_CLIENT_SECRET = os.environ['MEDIUM_CLIENT_SECRET']
    MEDIUM_PUBLICATION = os.environ['MEDIUM_PUBLICATION']
    MEDIUM_ME_ENDPOINT = os.environ['MEDIUM_ME_ENDPOINT']

    # Sendgrid
    SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
    SENDGRID_FROM_EMAIL = os.environ['SENDGRID_FROM_EMAIL']
    SENDGRID_TEMPLATE_ID = os.environ['SENDGRID_TEMPLATE_ID']

    # Mixpanel
    MIXPANEL_API_KEY = os.environ['MIXPANEL_API_KEY']
    MIXPANEL_API_SECRET = os.environ['MIXPANEL_API_SECRET']
    MIXPANEL_TOKEN = os.environ['MIXPANEL_TOKEN']

    # Aylien
    AYLIEN_APP_KEY = os.environ['AYLIEN_APP_KEY']
    AYLIEN_APP_ID = os.environ['AYLIEN_APP_ID']
