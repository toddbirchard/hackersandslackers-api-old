from flask import Flask
import sqlalchemy
from flask_sqlalchemy import Model, SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis

r = FlaskRedis()
db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
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
        r.set('token', app.config['TOKEN'])
        r.set('clientid', app.config['CLIENT_ID'])
        r.set('clientsecret', app.config['CLIENT_SECRET'])
        r.set('publication', app.config['PUBLICATION'])
        r.set('medium_endpoint_me', app.config['ME_ENDPOINT'])

        # Initialize Global db
        db.init_app(app)

        # HTML structure for new Lynx posts
        from . import previews

        # Construct the data set
        from . import routes

        return app
