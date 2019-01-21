import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.environ["TESTING"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    FLASK_DEBUG = os.environ["FLASK_DEBUG"]
    SESSION_TYPE = os.environ["SESSION_TYPE"]
    REDIS_URL = os.environ["FLASK", "REDIS_URL"]

    # Endpoint
    ENDPOINT = os.environ["ENDPOINTS", "PREVIEW"]
    DOMAIN = os.environ["ENDPOINTS", "DOMAIN"]

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
    TOKEN = os.environ['TOKEN']
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    PUBLICATION = os.environ['PUBLICATION']
    ME_ENDPOINT = os.environ['ME_ENDPOINT']

    # SendGridAPIClient
    SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
    SENDGRID_FROM_EMAIL = os.environ['FROM_EMAIL']
    SENDGRID_TEMPLATE_ID = os.environ['TEMPLATE_ID']
