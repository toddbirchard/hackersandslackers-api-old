from configparser import SafeConfigParser
import codecs
import os


class BaseConfig:
    """Build config from ini file."""

    def __init__(self):
        """Initialize configuration."""
        self.config = self.get_config()
        # Folders
        self.gcloud_endpoint = self.config.get('GCLOUD', 'ENDPOINT')
        # Database
        self.method = self.config.get('DB', 'METHOD')
        self.host = self.config.get('DB', 'HOST')
        self.user = self.config.get('DB', 'USER')
        self.password = self.config.get('DB', 'PASSWORD')
        self.port = self.config.get('DB', 'PORT')
        self.database = self.config.get('DB', 'DATABASE')
        self.query = self.config.get('DB', 'POST_QUERY')
        self.uri = self.method + self.user + ':' + self.password + '@' + self.host + '/' + self.database

    # Get self.configuration
    def get_config(self):
        """Read ini file."""
        parser = SafeConfigParser()
        abspath = os.path.dirname(__file__)
        config_path = os.path.join(abspath, "config.ini")
        with codecs.open(config_path, 'r', encoding='utf-8') as f:
            parser.readfp(f)
            return parser


config = BaseConfig()
