from flask import Flask
import sqlalchemy
from flask_sqlalchemy import Model, SQLAlchemy
from flask_redis import FlaskRedis

r = FlaskRedis()
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False, )
    app.config.from_object('config.Config')

    with app.app_context():
        # Set Global Session Variables
        r.init_app(app, charset="utf-8", decode_responses=True)
        r.set('endpoint', app.config['ENDPOINT'])
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('domain', app.config['DOMAIN'])
        r.set('query', app.config['POST_QUERY'])
        r.set('query_like', app.config['QUERY_LIKE'])

        # Set global contexts
        r.set('medium_token', app.config['MEDIUM_TOKEN'])
        r.set('medium_clientid', app.config['MEDIUM_CLIENT_ID'])
        r.set('medium_clientsecret', app.config['MEDIUM_CLIENT_SECRET'])
        r.set('medium_publication', app.config['MEDIUM_PUBLICATION'])
        r.set('medium_endpoint_me', app.config['MEDIUM_ME_ENDPOINT'])

        # MIXPANEL
        r.set('mixpanel_api_key', app.config['MIXPANEL_API_KEY'])
        r.set('mixpanel_api_secret', app.config['MIXPANEL_API_SECRET'])
        r.set('mixpanel_api_token', app.config['MIXPANEL_TOKEN'])

        # Initialize Global db
        db.init_app(app)

        # Construct the data set
        from . import models
        from . import account
        from . import syndication
        # from . import links
        from . import analytics

        return app
