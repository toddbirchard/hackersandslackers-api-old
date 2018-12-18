"""Configure for global app."""


class Config:
    """Build config from ini file."""

    # General
    TESTING = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    FLASK_DEBUG = True

    # Endpoint
    ENDPOINT = 'https://us-central1-hackersandslackers-204807.cloudfunctions.net/link-preview-endpoint?url='

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@a9tw3rjw35.185.3.216:3306/hackers_digitalocean_production'
    POST_QUERY = 'SELECT slug FROM posts WHERE title LIKE :lynx AND modified != 1;'
    QUERY_LIKE = '%%Lynx%%'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Apisentris
    ACCESS_TOKEN = 'bZwtWlISFmwd08xQJXrQAQ'
    CLIENT_ID = 103000
    HEADER_CONTENT_TYPE = 'application/json'
