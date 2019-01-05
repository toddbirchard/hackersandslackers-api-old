"""Configure for global app."""


class Config:
    """Build config from ini file."""

    # General
    TESTING = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    FLASK_DEBUG = True
    SESSION_TYPE = 'redis'
    REDIS_URL = "redis://:FHZwGXgLlUycqiSFRA3cEUqYFCwuR85i@redis-14084.c62.us-east-1-4.ec2.cloud.redislabs.com:14084/0"

    # Endpoint
    ENDPOINT = 'https://us-central1-hackersandslackers-204807.cloudfunctions.net/link-preview-endpoint?url='

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:a9tw3rjw@35.185.3.216:3306/hackers_digitalocean_production'
    SQLALCHEMY_ECHO = True

    POST_QUERY = "SELECT slug, html FROM posts WHERE title LIKE '%%Lynx%%'"
    QUERY_LIKE = "'%%Lynx%%'"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Apisentris
    ACCESS_TOKEN = 'bZwtWlISFmwd08xQJXrQAQ'
    CLIENT_ID = 103000
    HEADER_CONTENT_TYPE = 'application/json'
