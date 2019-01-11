import os
from configparser import SafeConfigParser


class Config:
    """Set Flask configuration vars from .ini file."""

    # Read config.ini
    configParser = SafeConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFilePath = (os.path.join(dir_path, 'config.ini'))
    configParser.read(configFilePath)

    # General
    TESTING = configParser.get("FLASK", "TESTING")
    SECRET_KEY = configParser.get("FLASK", "SECRET_KEY")
    FLASK_DEBUG = configParser.get("FLASK", "FLASK_DEBUG")
    SESSION_TYPE = configParser.get("FLASK", "SESSION_TYPE")
    REDIS_URL = configParser.get("FLASK", "REDIS_URL")

    # Endpoint
    ENDPOINT = configParser.get("ENDPOINTS", "PREVIEW")

    # Database
    SQLALCHEMY_DATABASE_URI = configParser.get("DATABASE", "SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = configParser.get("DATABASE", "SQLALCHEMY_ECHO")
    SQLALCHEMY_TRACK_MODIFICATIONS = configParser.get("DATABASE", "SQLALCHEMY_TRACK_MODIFICATIONS")

    # Queries
    POST_QUERY = configParser.get("QUERIES", "POST_QUERY")
    QUERY_LIKE = configParser.get("QUERIES", "QUERY_LIKE")


    # Apisentris
    ACCESS_TOKEN = configParser.get("APISENTRIS", "ACCESS_TOKEN")
    CLIENT_ID = configParser.get("APISENTRIS", "CLIENT_ID")
    HEADER_CONTENT_TYPE = configParser.get("APISENTRIS", "HEADER_CONTENT_TYPE")
